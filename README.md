# AI Healthcare Voice Assistant

An **AI-powered Healthcare Appointment Assistant** built using **Python and FastAPI** that allows users to interact through **text or voice commands** to manage doctor appointments.

The assistant can help users:

- Check available doctors
- View available appointment slots
- Book appointments
- Cancel appointments
- Interact using **API chat** or **voice assistant**

This project demonstrates how **conversational AI systems can automate healthcare appointment workflows**.

---

# Features

- Doctor availability check
- Slot availability checking
- Appointment booking
- Appointment cancellation
- Chat interaction via API
- Voice assistant interaction
- Session memory for conversations
- Fast response with latency tracking
- API testing using Swagger UI

---

# Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- SpeechRecognition
- PyAudio
- pyttsx3
- Langdetect
- Requests

---

# Project Structure

```
voice-ai-agent-project
│
├── agent/
│   ├── agent.py
│   ├── language.py
│   └── tools.py
│
├── campaigns/
│   └── campaign_worker.py
│
├── database/
│   ├── patients.json
│   └── appointments.json
│
├── memory/
│   ├── patient_memory.py
│   └── session_memory.py
│
├── scheduler/
│   └── appointment_engine.py
│
├── server/
│   └── main.py
│
├── voice_agent.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```
git clone https://github.com/Coding-Container/voice-ai-agent-project
cd voice-ai-agent-project
```

---

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

If microphone libraries fail on Windows install manually

```
pip install SpeechRecognition pyttsx3 pyaudio langdetect
```

---

# Running the Backend Server

Start the FastAPI server using Uvicorn.

```
python -m uvicorn server.main:app --reload
```

Server runs at

```
http://127.0.0.1:8000
```

---

# API Testing (Swagger UI)

Open browser:

```
http://127.0.0.1:8000/docs
```

Available endpoints

| Method | Endpoint | Description              |
| ------ | -------- | ------------------------ |
| GET    | /        | Server health check      |
| GET    | /chat    | Chat request using query |
| POST   | /chat    | Chat request using JSON  |

---

# Voice Assistant

The project includes a **voice assistant client** that allows users to speak commands instead of typing.

File used:

```
python voice_agent.py
```

The voice assistant workflow:

1. Listens to microphone input
2. Converts speech to text
3. Sends the request to the FastAPI backend
4. Receives the response
5. Speaks the response back to the user

---

#  Running the Voice Assistant

Make sure the backend server is already running.

Then run:

```
python voice_agent.py
```

Example interaction

```
Listening...

You: doctor
AI: Available doctors are Dr Ravi and Dr Priya

You: book appointment
AI: Appointment booked

You: cancel appointment
AI: Appointment cancelled
```

---

#  System Workflow

```
User Voice / Text
        │
        ▼
Voice Agent / API Request
        │
        ▼
FastAPI Backend
        │
        ▼
Agent Logic Processing
        │
        ▼
Scheduler & Database
        │
        ▼
Response Returned to User
```

---

#  Example API Response

```
{
  "response": "Appointment booked",
  "latency": 0.001
}



```
