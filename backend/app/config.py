import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB = os.getenv("MONGO_DB", "futurepath")

    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")

    PLACEMENT_MODEL_PATH = os.getenv("PLACEMENT_MODEL_PATH", "models/placement_model.pkl")
    CAMPUS_DATA_PATH = os.getenv("CAMPUS_DATA_PATH", "data/campus_recruitment.csv")
    JOBS_DATA_PATH = os.getenv("JOBS_DATA_PATH", "data/jobs_and_skills.csv")

    JWT_EXPIRES_MIN = int(os.getenv("JWT_EXPIRES_MIN", "120"))
