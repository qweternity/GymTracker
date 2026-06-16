from datetime import date
from pydantic import BaseModel

class ExerciseCreate(BaseModel):
    name: str
    date: date
    weight: float
    reps: int