import pandas as pd
import joblib

class PredictionService:
    def __init__(self, model_path: str = 'app/models/random_forest_model.pkl'):
        # Memuat model machine learning yang sudah dilatih
        self.model = joblib.load(model_path)

    def predict(self, data: pd.DataFrame):
        """Melakukan prediksi fraud berdasarkan data yang diunggah dalam file CSV"""
        # Hanya mengambil kolom yang diperlukan untuk prediksi
        features = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
        data_for_prediction = data[features]
        
        # Prediksi hasil
        predictions = self.model.predict(data_for_prediction)  # Mengambil prediksi biner (0 atau 1)
        probabilities = self.model.predict_proba(data_for_prediction)[:, 1]  # Mengambil probabilitas fraud
        
        # Menambahkan kolom baru ke DataFrame asli
        data['is_fraud'] = predictions  # Kolom prediksi (True/False)
        data['fraud_probability'] = probabilities  # Kolom probabilitas

        return data
