import base64
import io
import soundfile as sf

def decode_audio(audio_base64: str):
    """
    Decode base64 audio and return waveform + sample rate
    """
    audio_bytes = base64.b64decode(audio_base64)
    audio_buffer = io.BytesIO(audio_bytes)
    waveform, sample_rate = sf.read(audio_buffer)
    return waveform, sample_rate
