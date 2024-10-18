from pydantic import BaseModel

# Request Schema
class PredictionRequest(BaseModel):
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float

# Response schema
class PredictionResponse(BaseModel):
    is_fraud: bool
    probability: float