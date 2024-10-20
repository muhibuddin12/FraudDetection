from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.services.model_service import ModelService, get_model_service
from app.schemas.prediction import PredictionRequest, PredictionResponse
import pandas as pd
from typing import Dict
from app.interfaces.imodeltrainer import IModelTrainer
from app.utils.modeltrainer import RandomForestModelTrainer
from app.utils.dataloaderModel import CSVDataLoader
from app.services.file_service import FileService
from app.services.prediction_service import PredictionService
from io import StringIO
from fastapi.responses import StreamingResponse


app = FastAPI()
# Inisialisasi services
file_service = FileService()
prediction_service = PredictionService()

# Endpoint untuk memprediksi fraud
@app.post("/predict_fraud", response_model=PredictionResponse)
def predict_fraud(request: PredictionRequest, model_service: ModelService = Depends(get_model_service)):
    prediction = model_service.predict(request)
    return prediction

# Dependency Injection for training logic
def get_trainer() -> IModelTrainer:
    return RandomForestModelTrainer()


@app.post("/train/")
async def train_model(file: UploadFile = File(...)) -> Dict:
    try:
        # Load data
        data_loader = CSVDataLoader(file_path=file.file)
        data = data_loader.load_data()

        # Train model
        trainer = get_trainer()
        result = trainer.train(data)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/predict_fraud_file")
async def predict_fraud_file(file: UploadFile = File(...)) -> Dict:

   # Cek tipe file
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="File must be a CSV")

    # Proses file CSV
    data = await file_service.process_csv(file)

    # Lakukan prediksi
    predictions = prediction_service.predict(data)

     # Konversi hasil prediksi menjadi CSV
    output = StringIO()
    predictions.to_csv(output, index=False)
    output.seek(0)

    # Kirim file CSV sebagai respons
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=predictions.csv"})