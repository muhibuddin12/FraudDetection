from pydantic import BaseModel
from typing import List

class PredictionRequest(BaseModel):
    algorithm: str
    data: List[dict]
