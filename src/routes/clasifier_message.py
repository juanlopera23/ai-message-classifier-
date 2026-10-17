from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from google.genai.errors import ServerError, ClientError

from src.models import Message, ClassificationResponse
from ..gemini_service import interaction_genia

router = APIRouter()

next_id = 0

list_request = []


@router.post("/ask", response_model=ClassificationResponse)
async def clasifier_message(message: Message):

    global next_id

    try:

        interaction = await interaction_genia(message.ask)

    except ServerError as e:

        print(e)
        raise HTTPException(status_code=503, detail="Gemini Service Unavailable")

    except ClientError as e:

        raise HTTPException(status_code=503, detail="AI service request failed")

    try:
        ask = ClassificationResponse.model_validate_json(interaction.output_text)
        ask.id = next_id
        list_request.append(ask)
        next_id += 1
    except ValidationError:

        raise HTTPException(status_code=502, detail="validation error")

    return ask
