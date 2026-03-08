from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()

doctors = {
    "dr ravi": ["10am", "11am", "12pm"],
    "dr priya": ["2pm", "3pm", "4pm"]
}

appointments = {}

class ChatRequest(BaseModel):
    message: str


def process(text):

    text = text.lower()

    if "doctor" in text:
        return "Available doctors are Dr Ravi and Dr Priya."

    if "slot" in text:
        return "Available slots for Dr Ravi: 10am, 11am, 12pm"

    if "book" in text:
        key = "dr ravi_10am"

        if key in appointments:
            return "Slot already booked"

        appointments[key] = True
        return "Appointment booked"

    if "cancel" in text:
        key = "dr ravi_10am"

        if key in appointments:
            del appointments[key]
            return "Appointment cancelled"

        return "No appointment found"

    return "Ask about doctors, slots, booking or cancellation."


@app.get("/")
def home():
    return {"message": "Healthcare Voice AI Agent running"}


# GET endpoint
@app.get("/chat")
def chat(q: str):

    start = time.time()

    response = process(q)

    latency = time.time() - start

    return {
        "response": response,
        "latency": latency
    }


# POST endpoint
@app.post("/chat")
def chat_post(data: ChatRequest):

    start = time.time()

    response = process(data.message)

    latency = time.time() - start

    return {
        "response": response,
        "latency": latency
    }