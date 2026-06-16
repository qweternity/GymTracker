from fastapi import FastAPI

import gym
from requests import ExerciseCreate
import models

app = FastAPI(title="Gym Tracker")


@app.get("/")
def root():
    return {"message": "Gym Tracker API"}

@app.post("/exercise")
def create_exercise(data: ExerciseCreate):
    dto = models.ExerciseCreateDTO(
        data.name, data.date, data.weight, data.reps
    )

    exercise = gym.create_exercise(dto)
    return {"exercise": exercise}
