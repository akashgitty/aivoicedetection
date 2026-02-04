from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64

app = FastAPI()

class AudioRequest(BaseModel):
    audio_base64: str

@app.post("/detect")
async def detect_voice(request: AudioRequest):
    try:
        # Decode Base64 safely
        decoded_audio = base64.b64decode(request.audio_base64)

        # Dummy response (safe + valid)
        return {
            "classification": "HUMAN",
            "confidence": 0.95
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
