# app.py
from fastapi import FastAPI, Request
from agents import Agent, Runner

app = FastAPI()

agent = Agent(
    name="Friendly Assistant",
    instructions="""
You are a friendly, personable assistant who loves memes and jokes. Be upbeat, casual, and fun, especially about electric cars!
"""
)

@app.get("/")
def root():
    return {"message": "FastAPI chatbot is running."}

@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    user_input = data.get("message", "")

    if not user_input:
        return {"error": "No message received."}

    result = await Runner.run(agent, f"You: {user_input}")
    response = result.final_output

    return {"reply": response}
