from datetime import date
from dataclasses import dataclass
from bson import ObjectId

@dataclass
class ExersiceEntity:
    name: str
    date: date
    weight: float
    reps: int
    id : ObjectId = None

@dataclass
class ExerciseCreateDTO:
    name: str
    date: date
    weight: float
    reps: int