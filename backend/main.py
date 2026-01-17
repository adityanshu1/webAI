from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import os

app = FastAPI()

with open("backend/identity.txt", "r") as f:
    SYSTEM_IDENTITY = f.read()

class Query(BaseModel):
    message: str

def ask_ai(prompt):
    full_prompt = SYSTEM_IDENTITY + "\nUser: " + prompt
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=full_prompt,
        text=True,
        capture_output=True
    )
    return result.stdout

@app.post("/chat")
def chat(query: Query):
    return {"response": ask_ai(query.message)}
