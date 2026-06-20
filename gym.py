from pymongo.errors import DuplicateKeyError

import database
import schemas
from models import ExerciseEntity

def create_exercise(dto: schemas.ExerciseCreate):
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
        result.append({
            "name": exercise["name"],
            "date": exercise["date"],
            "weight": exercise["weight"],
            "reps": exercise["reps"]
        })
    return result

def delete_exercise(name: str):
    exercise = database.exercises.delete_one({"name": name})
    if exercise.deleted_count == 0:
        return None
    else:
        return f"Exercise {name} deleted successfully"

def update_exercise(dto: schemas.ExerciseUpdateWeight):
    result = database.exercises.update_one(
        {"name": dto.name},
        {"$set": {"weight": dto.weight, "reps": dto.reps}},
    )
    if result.modified_count == 0:
        return None
    return f"Exercise {dto.name} updated successfully"