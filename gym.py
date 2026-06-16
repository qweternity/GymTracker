import database
from models import ExerciseCreateDTO, ExersiceEntity

def create_exercise(dto: ExerciseCreateDTO):
    entity = ExersiceEntity(
        name=dto.name,
        date=dto.date,
        weight=dto.weight,
        reps=dto.reps
    )
    database.exercises_collection.insert_one({
        "name": dto.name,
        "date": dto.date,
        "weight": dto.weight,
        "reps": dto.reps
    })