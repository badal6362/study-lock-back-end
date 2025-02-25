from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from database import get_db
from models import StudySession

router = APIRouter()

@router.post("/start")
def start_session(user_id: str, db: Session = Depends(get_db)):
    session = StudySession(user_id=user_id, start_time=datetime.utcnow())
    db.add(session)
    db.commit()
    db.refresh(session)
    return {"message": "Session started", "session_id": session.id}
