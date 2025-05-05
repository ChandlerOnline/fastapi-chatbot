from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Define the internal route path, not the Make.com URL
@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    print("Received data:", data)

    last_input = data.get("last_input_text", "No input found")

    return {
        "reply": f"Received your message: {last_input}"
    }

