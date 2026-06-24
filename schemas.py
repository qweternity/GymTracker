from datetime import datetime
from pydantic import BaseModel

class ExerciseCreate(BaseModel):
    name: str
    date: datetime
    weight: float
    reps: int

class ExerciseGet(BaseModel):
    name: str

class ExerciseUpdateWeightRequest(BaseModel):
    weight: float
    reps: int