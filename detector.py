import torch
import soundfile as sf
from transformers import Wav2Vec2Processor, Wav2Vec2Model

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base")
model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base")
model.eval()

def detect_ai(audio_bytes):
    audio, sr = sf.read(audio_bytes)
    inputs = processor(audio, sampling_rate=sr, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    score = torch.sigmoid(outputs.last_hidden_state.mean()).item()

    if score > 0.5:
        return "AI_GENERATED", round(score, 2)
    return "HUMAN", round(1 - score, 2)
