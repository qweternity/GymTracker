import database
import schemas
from models import ExerciseEntity

def create_exercise(dto: schemas.ExerciseCreate):
    catalog = database.exercises.find()
    entity = ExerciseEntity(
        name=dto.name,
        date=dto.date,
        weight=dto.weight,
        reps=dto.reps
    )
    database.exercises.insert_one({
        "name": entity.name,
        "date": entity.date,
        "weight": entity.weight,
        "reps": entity.reps
    })

def show_exercises():
    diary = database.exercises.find()
    result = []
    for exercise in diary:
        entity = ExerciseEntity(
            name=exercise["name"],
            date=exercise["date"],
            weight=exercise["weight"],
            reps=exercise["reps"]
        )
        result.append(entity)
    return result

def delete_exercise(dto: schemas.ExerciseGet):
    exercise = database.exercises.delete_one({"name": dto.name})
    return exercise

def update_exercise(dto: schemas.ExerciseUpdateWeight):
    database.exercises.update_one(
        {"name": dto.name},
        {"$set": {"weight": dto.weight, "reps": dto.reps}},
    )