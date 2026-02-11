import json
import stripe
from fastapi import APIRouter, Request

router = APIRouter()

stripe.api_key = "sk_live_..."

@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()

    event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key
    )

    return {"status": "success"}
