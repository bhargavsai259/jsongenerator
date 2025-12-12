from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from groq import Groq
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.get("/stream")
async def stream_llm(prompt: str):

    def generate():
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "i should create read me file for the text i received only no more extra data"},
                      {"role": "user", "content": prompt}],
            stream=True
        )

        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    return StreamingResponse(generate(), media_type="text/plain")
