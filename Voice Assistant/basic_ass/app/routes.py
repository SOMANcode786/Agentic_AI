from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from app import services

router = APIRouter()

@router.post("/voice")
async def process_voice(audio: UploadFile = File(...)):
    return await services.handle_voice(audio)
