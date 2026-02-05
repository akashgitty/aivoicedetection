# AI Voice Detection API

FastAPI based API for detecting AI generated voices.

## Endpoint
POST /detect

## Authentication
Header:
x-api-key: mysecretkey123

## Request
{
  "language": "english",
  "audioFormat": "mp3",
  "audioBase64": "BASE64_STRING"
}

## Response
{
  "classification": "HUMAN",
  "confidence": 0.95
}
