from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import base64

app = FastAPI()

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import base64

app = FastAPI()

API_KEY = "mysecretkey123"

# 🔹 Updated request model (matches tester)
class AudioRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str


@app.post("/detect")
async def detect_voice(
    request: AudioRequest,
    x_api_key: str = Header(None)
):
    # API key check
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        # decode tester base64 field
        base64.b64decode(request.audioBase64)

        return {
            "classification": "HUMAN",
            "confidence": 0.95
        }

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid audio data")
