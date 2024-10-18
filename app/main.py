from fastapi import FastAPI, Depends
from pydantic import BaseModel
from services.model_service import ModelService, get_model_service
from schemas.prediction import PredictionRequest, PredictionResponse


app = FastAPI()

# Endpoint untuk memprediksi fraud
@app.post("/predict_fraud", response_model=PredictionResponse)
def predict_fraud(request: PredictionRequest, model_service: ModelService = Depends(get_model_service)):
    prediction = model_service.predict(request)
    return prediction
