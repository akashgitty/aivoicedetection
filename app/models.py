from pydantic import BaseModel, Field

class VoiceInput(BaseModel):
    language: str
    # Use 'alias' to tell FastAPI to look for the names the tester uses
    audio_format: str = Field(alias="audioFormat")
    audio_base_64: str = Field(alias="audioBase64")

    class Config:
        populate_by_name = True