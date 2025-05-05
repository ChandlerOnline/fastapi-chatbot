from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    # Get the incoming JSON data
    data = await request.json()

    # Print the received data to the console
    print("Received data:", json.dumps(data, indent=4))

    # Return a simple response confirming the data was received
    return {
        "status": "Received",
        "received_data": data
    }
