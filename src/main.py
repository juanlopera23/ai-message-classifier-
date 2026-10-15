from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from google import genai
from datetime import  date

from src.models import Message, ClassificationResponse
from src.prompts import SYSTEM_INSTRUCTIONS

client = genai.Client()

app = FastAPI()

list_messages=[]

next_id = 0

 

@app.post("/request", response_model=ClassificationResponse)
async def clasifier_message (message : Message):

    today = date.today()

    try:

        interaction = await client.aio.interactions.create(

            model="gemini-3.1-flash-lite",
            system_instruction = f"""
                CURRENT DATE: {today}
                {SYSTEM_INSTRUCTIONS}
                """,
            input= message.ask,
            response_format={
                "type" : "text",
                "mime_type" : "application/json",
                "schema" : ClassificationResponse.model_json_schema()
            }
        )
    except Exception as e:

        print(f"Gemini error: {type(e).__name__}: {e}")
        raise HTTPException(
            status_code= 503,
            detail="Gemini Service Unavailable"
        )

    try:
        ask = ClassificationResponse.model_validate_json(interaction.output_text)
    except ValidationError :

        raise HTTPException(
            status_code= 502,
            detail="validation error"
        )


    return ask

@app.get("/request")
async def list_messages():

    return list_messages

@app.get("/request/{message_id}")
async def search(message_id : int):

    for item in list_messages:
        if item.id == message_id:
            return item

    raise HTTPException(
        status_code= 404,
        detail="not found"
    )

@app.delete("/request/{message_id}")
async def search(message_id : int):

    for item in list_messages:
        if item.id == message_id:
            list_messages.remove(item)
            return list_messages

    raise HTTPException(
        status_code= 404,
        detail="not found"
    )

