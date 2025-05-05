from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    print("Received data:", data)

    # Extract the message text (based on what you said you're receiving)
    last_input = data.get("last_input_text", "No input found")

    # Return a simple JSON response
    return {
        "reply": f"Received your message: {last_input}"
    }
