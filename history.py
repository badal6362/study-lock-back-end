from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import StudySession

router = APIRouter()

@router.get("/history")
def get_history(user_id: str, db: Session = Depends(get_db)):
    sessions = db.query(StudySession).filter(StudySession.user_id == user_id).all()
    return sessions
