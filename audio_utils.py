import base64
import io

def decode_audio(base64_string):
    audio_bytes = base64.b64decode(base64_string)
    return io.BytesIO(audio_bytes)
