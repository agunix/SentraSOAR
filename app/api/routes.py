from fastapi import APIRouter
from app.models.event import Event
from app.engine.rule_engine import process_event
from app.storage.memory_db import db

router = APIRouter()

@router.post("/event")
def ingest_event(event: Event):
    result = process_event(event)
    return result


@router.get("/alerts")
def get_alerts():
    return db.alerts


@router.get("/incidents")
def get_incidents():
    return db.incidents