from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import base64
from typing import Optional
import time


app = FastAPI()

API_KEY = "mysecretkey123"

class AudioRequest(BaseModel):
    language: Optional[str] = None
    audioFormat: Optional[str] = None
    audioBase64: str

@app.post("/detect")
async def detect_voice(
    request: AudioRequest,
    x_api_key: str = Header(None, alias="x-api-key")
):

    start_time = time.time()

    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        base64.b64decode(request.audioBase64)
    except:
        raise HTTPException(status_code=400, detail="Invalid Base64")

    latency = round(time.time() - start_time, 4)
    print(f"Request processed in {latency} seconds")

    return {
        "classification": "HUMAN",
        "confidence": 0.95,
        "latency": latency
    }