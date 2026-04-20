from fastapi import FastAPI
from pydantic import BaseModel
import os

# If using OpenAI / Gemini etc.
# from openai import OpenAI

app = FastAPI()

class Query(BaseModel):
    prompt: str

# Example placeholder function (replace with real LLM call)
def call_llm(prompt: str):
    # Replace this with OpenAI/Gemini/etc.
    return f"Echo: {prompt}"

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(query: Query):
    response = call_llm(query.prompt)
    return {"response": response}