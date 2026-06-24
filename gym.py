from dataclasses import asdict
from bson import ObjectId

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
    database.exercises.insert_one(asdict(entity)) # asdict() - преобразует dataclasses в словарь

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

def update_exercise_by_id(_id: str, dto: schemas.ExerciseUpdateWeightRequest):
    result = database.exercises.update_one(
        {"_id": ObjectId(_id)},
        {"$set": {"weight": dto.weight, "reps": dto.reps}},
    )
    if result.modified_count == 0:
        return None
    return f"Exercise {_id} updated successfully"

def find_by_name(name: str):
    result = []
    exercises = database.exercises.find({"name": name})
    for exercise in exercises:
        result.append({
            "name": exercise["name"],
            "date": exercise["date"],
            "weight": exercise["weight"],
            "reps": exercise["reps"],
            "id": str(exercise["_id"])
        })
    return result

def delete_by_id(_id: str):
    deleted = database.exercises.delete_one({"_id": ObjectId(_id)})
    if deleted.deleted_count == 0:
        return None
    return f"Exercise {_id} deleted successfully"