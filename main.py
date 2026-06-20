from fastapi import FastAPI
from pymongo.errors import DuplicateKeyError

import gym
import schemas
from schemas import ExerciseCreate, ExerciseGet, ExerciseUpdateWeight, ExerciseUpdateWeightRequest

app = FastAPI(title="Gym Tracker")


@app.get("/")
def root():
    return {"message": "Gym Tracker API"}

@app.post("/exercises")
def add_exercise(data: ExerciseCreate):
    try:
        gym.create_exercise(data)
        return f"exercise created: {data.name}"
    except DuplicateKeyError:
        return {"exercise already exists": data.name}

@app.get("/exercises")
def show_exercises():
    exercises = gym.show_exercises()
    return {"exercises": exercises}

@app.delete("/exercises/{name}")
def delete_exercise(name: str):
    deleted = gym.delete_exercise(name)
    if deleted is None:
        return {"Exercise not found": name}
    return {"exercise deleted": name}

@app.put("/exercises/{name}")
def update_exercise(name, data: ExerciseUpdateWeightRequest):
    dto = schemas.ExerciseUpdateWeight(name=name, weight=data.weight, reps=data.reps)
    updated = gym.update_exercise(dto)
    if updated is None:
        return {"Exercise not found": name}
    return {"exercise updated": updated}