from services.api_service import ApiService
from models.model_selection import ModelSelection

class PredictionService:
    def __init__(self, api_service: ApiService):
        self.api_service = api_service

    def predict(self, algorithm, uploaded_file):
        """Melakukan prediksi berdasarkan algoritma yang dipilih"""
        # Dapatkan model yang sesuai dari ModelSelection
        model = ModelSelection.get_model(algorithm)

        # Kirim data ke API untuk prediksi
        predictions = self.api_service.send_data_for_prediction(uploaded_file)
        return predictions
