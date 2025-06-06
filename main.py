from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Correct placement of the actual key in URL
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ In production, replace "*" with your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"message": "Backend working. Use /ask to send a question."}

@app.post("/ask")
def ask_gemini(query: Query):
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": query.question}
                ]
            }
        ]
    }

    response = requests.post(GEMINI_URL, json=payload, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            return {
                "answer": data["candidates"][0]["content"]["parts"][0]["text"]
            }
        except Exception:
            return {"answer": "⚠️ Gemini response format changed or was empty."}
    else:
        return {
            "answer": f"❌ Error: {response.status_code} - {response.text}"
        }
