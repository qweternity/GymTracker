from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["gymtracker"]
exercises_collection = db["exercises"]