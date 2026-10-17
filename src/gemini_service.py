from google import genai
from datetime import date


from src.models import ClassificationResponse
from src.prompts import SYSTEM_INSTRUCTIONS

client = genai.Client()


async def interaction_genia(message):

    today = date.today()

    interaction = await client.aio.interactions.create(
        model="gemini-3.1-flash-lite",
        system_instruction=f"""
            CURRENT DATE: {today}
            {SYSTEM_INSTRUCTIONS}
        """,
        input=message,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": ClassificationResponse.model_json_schema(),
        },
    )
    return interaction
