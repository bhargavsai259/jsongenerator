from groq import Groq
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt:str


app = FastAPI()



@app.post("/generate_json")
async def generate_json(request:PromptRequest):
    return {'received prompt':request.prompt}