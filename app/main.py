from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import base64

app = FastAPI()

API_KEY = "mysecretkey123"


class AudioRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str


@app.post("/detect")
async def detect_voice(request: AudioRequest, x_api_key: str = Header(None)):

    # API Key Check
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        # Decode base64 safely
        base64.b64decode(request.audioBase64)

        return {
            "classification": "HUMAN",
            "confidence": 0.95
        }

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid audio")
