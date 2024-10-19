from abc import ABC, abstractmethod
import pandas as pd

class IModelTrainer(ABC):
    @abstractmethod
    def train(self, data: pd.DataFrame):
        pass
