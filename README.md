# AI Message Classifier

AI-powered REST API built with FastAPI, Google Gemini, and Pydantic to classify customer messages, identify user intents, extract appointment information, and return validated structured JSON responses.

## 1. Project Overview

AI Message Classifier is a Python backend application designed to interpret natural language messages in a business appointment management context.

The application uses Google Gemini to analyze customer requests and identify the intended action, along with relevant information such as appointment dates and times.

Pydantic validates the extracted data to ensure that API responses follow a consistent structure.

Core principle: AI interprets user requests; Python validates and controls the application logic.

This project focuses on intent classification and information extraction. It does not create, cancel, or reschedule real appointments.

## Features

- AI-powered intent classification using Gemini.
- Structured JSON responses.
- Date extraction and normalization (`YYYY-MM-DD`).
- Time extraction and validation (`HH:MM`).
- Input and output validation with Pydantic.
- Asynchronous API requests and error handling.
- Modular architecture using FastAPI `APIRouter`.

## Supported Intents

| Intent | Description |
|---|---|
| `create_appointment` | Schedule an appointment |
| `cancel_appointment` | Cancel an appointment |
| `check_availability` | Check availability |
| `reschedule_appointment` | Reschedule an appointment |
| `unknown` | Unknown or unclear request |

## Technologies

- Python 3.10+
- FastAPI
- Pydantic
- Google Gemini API
- Uvicorn

## Project Structure

```text
src/
├── main.py
├── models.py
├── prompts.py
├── gemini_service.py
└── routes/
    ├── clasifier_message.py
    └── requests.py
```

## Installation

**1. Clone the repository**

```bash
git clone <repository-url>
cd 3_ai_message_classifier
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure your Gemini API key**

```bash
export GEMINI_API_KEY="your_api_key"
```

**5. Run the application**

```bash
uvicorn src.main:app --reload
```

Access Swagger UI at:

`http://127.0.0.1:8000/docs`

## API Example

**Endpoint:** `POST /ask`

Request:

```json
{
  "ask": "Quiero reservar una cita mañana a las 5 de la tarde"
}
```

Example response (assuming today is October 14, 2026):

```json
{
  "intent": "create_appointment",
  "date": "2026-10-15",
  "time": "17:00"
}
```

## Error Handling

| HTTP Code | Description |
|---|---|
| 200 | Successful request |
| 422 | Invalid input |
| 502 | Invalid AI response |
| 503 | External AI service error |

## Architecture

The application follows this workflow:

**Client → FastAPI → Pydantic → Gemini → Structured Output → Pydantic Validation → HTTP Response**

The AI interprets customer requests, while Python validates the information and controls application behavior.

## Limitations

- No database persistence.
- No real appointment management.
- In-memory records are lost when the server restarts.
- No production authentication or rate limiting.

This project focuses on **AI message classification, structured outputs, validation, and modular backend development**.

---

**Project 3 — AI Automation Learning Path**