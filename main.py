from groq import Groq
from dotenv import load_dotenv
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}






