import joblib
import numpy as np
from app.schemas.prediction import PredictionRequest, PredictionResponse

class ModelService:
    def __init__(self, model_path: str):
        # Load model saat inisialisasi
        self.model = joblib.load(model_path)
    
    def predict(self, request: PredictionRequest) -> PredictionResponse:
        # konversi request kedalam array
        data = np.array(
            [[
                request.amount,
                request.oldbalanceOrg,
                request.newbalanceOrig,
                request.oldbalanceDest,
                request.newbalanceDest
            ]]
        )

        #Prediksi hasil
        prediction = self.model.predict(data)
        probability = self.model.predict_proba(data)[0][1]

        #Return hasil sebagai response schema
        return PredictionResponse(is_fraud=bool(prediction[0]), probability=probability)
    
# Dependency Injection untuk service
def get_model_service():
    model_path = 'models/random_forest_model.pkl'
    return ModelService(model_path)

