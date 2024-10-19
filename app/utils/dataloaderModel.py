import pandas as pd

from app.interfaces.dataloader import IDataLoader

class CSVDataLoader(IDataLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)
