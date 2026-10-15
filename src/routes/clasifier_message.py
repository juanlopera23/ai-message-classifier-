from fastapi import APIRouter, HTTPException
from  pydantic import ValidationError
from google import genai
from datetime import date

from src.models import Message,ClassificationResponse
from src.prompts import SYSTEM_INSTRUCTIONS

client = genai.Client()

router = APIRouter

@router.post("/ask", response_model= ClassificationResponse)
async def clasifier_message (message : Message):

    today = date.today()

    try :

        