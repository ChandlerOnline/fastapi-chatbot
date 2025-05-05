from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    print("Received data:", json.dumps(data, indent=4))

    return {
        "status": "Received",
        "received_data": data
    }

