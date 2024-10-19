from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from app.interfaces.imodeltrainer import IModelTrainer
import pandas as pd

class RandomForestModelTrainer(IModelTrainer):
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, data: pd.DataFrame):
        X = data.drop("isFraud", axis=1)
        y = data["isFraud"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return {"accuracy": accuracy}
