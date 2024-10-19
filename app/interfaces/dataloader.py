from abc import ABC, abstractmethod
import pandas as pd

class IDataLoader(ABC):
    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        pass
