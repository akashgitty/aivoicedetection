from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import base64

app = FastAPI()

# Your API KEY
API_KEY = "mysecretkey123"

class AudioRequest(BaseModel):
    audio_base64: str

@app.post("/detect")
async def detect_voice(
    request: AudioRequest,
    x_api_key: str = Header(None)
):
    # 🔐 API Key check
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        decoded_audio = base64.b64decode(request.audio_base64)

        return {
            "classification": "HUMAN",
            "confidence": 0.95
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
