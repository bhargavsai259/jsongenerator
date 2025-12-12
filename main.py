from groq import Groq
from dotenv import load_dotenv
import os
import json
from fastapi import FastAPI
from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt:str


app = FastAPI()

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.post("/generate_json")
async def generate_json(request: PromptRequest):
    prompt_text = request.prompt
    try:
        # Correct API call
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a JSON generator. Always return ONLY valid JSON. No code blocks. No backticks."
                },
                {"role": "user", "content": prompt_text}
            ]
        )

        # Extract AI-generated text
        generated_text = response.choices[0].message.content
        s=json.loads(generated_text)
        return s

    except Exception as e:
        return {"error": str(e)}
