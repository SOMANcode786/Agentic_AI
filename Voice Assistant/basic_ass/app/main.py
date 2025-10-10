import os
from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from app.services import process_audio

load_dotenv()  # load API key

app = FastAPI()

# serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return {"message": "✅ FastAPI Voice Agent Running!"}

@app.post("/voice")
async def voice(audio: UploadFile = File(...)):
    return await process_audio(audio)
