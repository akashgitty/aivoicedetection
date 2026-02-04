from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import base64
from typing import Optional

app = FastAPI()

API_KEY = "mysecretkey123"

class AudioRequest(BaseModel):
    language: Optional[str] = None
    audioFormat: Optional[str] = None
    audioBase64: str

@app.post("/detect")
async def detect_voice(request: AudioRequest, x_api_key: str = Header(None)):
    
    # ✅ API KEY CHECK
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        # decode audio safely
        decoded_audio = base64.b64decode(request.audioBase64)

        # dummy response
        return {
            "classification": "HUMAN",
            "confidence": 0.95
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
