import requests
from models.fraud_input import FraudInput

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
        
    def send_data_for_prediction(self, uploaded_file):
        url = f"{self.api_url}/predict_fraud_file"
        # Baca file CSV
        csv_file = uploaded_file.getvalue()

        # Kirim file ke API sebagai multipart form
        files = {
            'file': (uploaded_file.name, csv_file, 'text/csv')
        }
        response = requests.post(url, files=files)

        # Jika berhasil, respons berupa CSV
        if response.status_code == 200:
            # Respons dalam bentuk file CSV
            return response.content
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

# Dependency Injection untuk ApiService
def get_api_service():
    api_url = "http://127.0.0.1:8000"  # API FastAPI yang sudah dibuat sebelumnya
    return ApiService(api_url)
