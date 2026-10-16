from fastapi import APIRouter, HTTPException

from src.routes.clasifier_message import list_request

router = APIRouter()

@router.get("/request")

async def list_messages():

    return list_request

@router.get("/request/{message_id}")
async def search(message_id : int):

    for item in list_request:
        if item.id == message_id:
            return item

    raise HTTPException(
        status_code= 404,
        detail="not found"
    )

@router.delete("/request/{message_id}")
async def search(message_id : int):

    for item in list_request:
        if item.id == message_id:
            list_request.remove(item)
            return list_request

    raise HTTPException(
        status_code= 404,
        detail="not found"
    )

