import pandas as pd

class FraudModelInterface:
    def train(self, data: pd.DataFrame):
        raise NotImplementedError

    def predict(self, data: pd.DataFrame) -> pd.Series:
        raise NotImplementedError

    def download_predictions(self, predictions: pd.Series) -> None:
        raise NotImplementedError
