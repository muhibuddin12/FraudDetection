import requests
from schemas.ui_input import FraudInput

class ApiService:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def predict_fraud(self, input_data: FraudInput):
        # Mengirimkan request ke API FastAPI untuk prediksi
        response = requests.post(f"{self.api_url}/predict_fraud", json=input_data.dict())
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to predict fraud"}

# Dependency Injection untuk ApiService
def get_api_service():
    api_url = "http://127.0.0.1:8000"  # API FastAPI yang sudah dibuat sebelumnya
    return ApiService(api_url)
