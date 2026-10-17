from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from google import genai
from datetime import date

from src.models import Message, ClassificationResponse
from src.prompts import SYSTEM_INSTRUCTIONS
from src.routes.clasifier_message import router as clasifier_message_router
from src.routes.requests import router as request_router

client = genai.Client()

app = FastAPI()

app.include_router(clasifier_message_router)
app.include_router(request_router)
