from fastapi import FastAPI
from pymongo.errors import DuplicateKeyError

import gym
import schemas
from schemas import ExerciseCreate, ExerciseUpdateWeightRequest

app = FastAPI(title="Gym Tracker")


@app.get("/")
def root():
    return {"message": "Gym Tracker API"}

@app.post("/exercises")
def add_exercise(data: ExerciseCreate):
    gym.create_exercise(data)
    return f"exercise created: {data.name}"

@app.get("/exercises")
def show_exercises():
    exercises = gym.show_exercises()
    return {"exercises": exercises}

@app.put("/exercises/{_id}")
def update_exercise_by_id(_id, data: ExerciseUpdateWeightRequest):
    dto = schemas.ExerciseUpdateWeightRequest(weight=data.weight, reps=data.reps)
    updated = gym.update_exercise_by_id(_id, data)
    if updated is None:
        return {"Exercise not found": _id}
    return {"exercise updated": updated}

@app.get("/exercises/{name}")
def get_exercise_by_name(name: str):
    exercises = gym.find_by_name(name)
    return {"exercises": exercises}

@app.delete("/exercises/{_id}")
def delete_exercise_by_name(_id: str):
    deleted = gym.delete_by_id(_id)
    if deleted is None:
        return {"Exercise not found": _id}
    return {"deleted": deleted}