import random

def detect_ai(waveform, sample_rate):
    """
    Dummy AI voice detector.
    Replace with real model later.
    """
    confidence = round(random.uniform(0.6, 0.95), 2)
    classification = "AI_GENERATED" if confidence > 0.75 else "HUMAN"
    return classification, confidence
