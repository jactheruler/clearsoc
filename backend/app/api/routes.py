from fastapi import APIRouter
from typing import List
from app.models.event import SecurityEvent

router = APIRouter()

events: List[SecurityEvent] = []


@router.post("/ingest")
def ingest_event(event: SecurityEvent):
    events.append(event)
    return {
        "status": "event received",
        "total_events": len(events)
    }


@router.get("/events")
def get_events():
    return events
