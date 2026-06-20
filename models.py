from datetime import date
from dataclasses import dataclass
from bson import ObjectId

@dataclass
class ExerciseEntity:
    name: str
    date: date
    weight: float
    reps: int
    id : ObjectId = None