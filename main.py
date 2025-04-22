from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI + Replit + Render!"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}