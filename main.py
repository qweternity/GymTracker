from fastapi import FastAPI
from pygments.lexers import data

import gym
import schemas
from schemas import ExerciseCreate, ExerciseGet, ExerciseUpdateWeight, ExerciseUpdateWeightRequest

app = FastAPI(title="Gym Tracker")


@app.get("/")
def root():
    return {"message": "Gym Tracker API"}

@app.post("/exercises")
def add_exercise(data: ExerciseCreate):
    gym.create_exercise(data)
    return {"exercise added": data}

@app.get("/exercises")
def show_exercises():
    exercises = gym.show_exercises()
    return {"exercises": exercises}

@app.delete("/exercises/{name}")
def delete_exercise(data: ExerciseGet):
    gym.delete_exercise(data)
    return {"exercise deleted": data}

@app.put("/exercises/{name}")
def update_exercise(name, data: ExerciseUpdateWeightRequest):
    dto = schemas.ExerciseUpdateWeight(name=name, weight=data.weight, reps=data.reps)
    updated = gym.update_exercise(dto)
    return {"exercise updated": updated}