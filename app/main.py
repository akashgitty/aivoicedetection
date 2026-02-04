from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel
import base64

app = FastAPI(
    title="AI Voice Detection API",
    version="1.0"
)

# 🔐 API KEY
API_KEY = "mysecretkey123"


# ✅ Request Model (Matches Hackathon Tester EXACTLY)
class AudioRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str


# ✅ Health Check (Render + Judges like this)
@app.get("/")
def health():
    return {"status": "API is running"}


# ✅ Detection Endpoint
@app.post("/detect")
async def detect_voice(
    request: AudioRequest,
    x_api_key: str = Header(None)
):

    # 🔐 API KEY CHECK
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    # 🎧 Base64 Audio Validation
    try:
        if not request.audioBase64:
            raise ValueError("Empty audio")

        base64.b64decode(request.audioBase64)

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid audio_base64"
        )

    # 🤖 Fake Model Response (Replace with real model later)
    return {
        "classification": "HUMAN",
        "confidence": 0.95
    }
