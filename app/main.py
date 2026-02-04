from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import base64
import os

app = FastAPI()

API_KEY = os.getenv("API_KEY", "mysecretkey123")

class AudioRequest(BaseModel):
    audioBase64: str
    language: str | None = None
    audioFormat: str | None = None

@app.post("/detect")
async def detect_voice(
    request: AudioRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        base64.b64decode(request.audioBase64)

        return {
            "classification": "HUMAN",
            "confidence": 0.95
        }

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid audio")

