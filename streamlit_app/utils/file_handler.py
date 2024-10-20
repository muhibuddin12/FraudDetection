import pandas as pd
import io

def download_csv(predictions):
    """Mengonversi hasil prediksi menjadi file CSV yang bisa diunduh"""
    df = pd.DataFrame(predictions)
    csv = io.StringIO()
    df.to_csv(csv, index=False)
    csv.seek(0)
    return csv.getvalue()
