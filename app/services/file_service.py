from fastapi import UploadFile
import pandas as pd
from io import StringIO

class FileService:
    async def process_csv(self, file: UploadFile) -> pd.DataFrame:
        """Memproses file CSV yang diunggah menjadi DataFrame"""
        try:
            # Read the contents of the uploaded file
            contents = await file.read()
            
            # Decode the file contents and process with pandas
            data = pd.read_csv(StringIO(contents.decode('utf-8')))
            return data
        
        except pd.errors.EmptyDataError:
            raise ValueError("The uploaded file is empty or contains no data.")
        except Exception as e:
            raise ValueError(f"An error occurred while processing the CSV: {str(e)}")
