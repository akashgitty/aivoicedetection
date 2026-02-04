from fastapi import FastAPI
from app.models import AudioRequest
from app.audio_utils import decode_audio

app = FastAPI()

@app.post("/detect")
async def detect_voice(request: AudioRequest):
    audio = decode_audio(request.audio_base64)
    return {
        "classification": "HUMAN",
        "confidence": 0.99
    }
