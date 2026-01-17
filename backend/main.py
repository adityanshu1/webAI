from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


with open("identity.txt", "r") as f:
    SYSTEM_IDENTITY = f.read()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

class Query(BaseModel):
    message: str

def ask_ai(prompt):
    payload = {
        "inputs": SYSTEM_IDENTITY + "\nUser: " + prompt
    }
    response = requests.post(MODEL_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]

@app.post("/chat")
def chat(query: Query):
    return {"response": ask_ai(query.message)}
