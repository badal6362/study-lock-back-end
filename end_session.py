from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from database import get_db
from models import StudySession

router = APIRouter()

@router.post("/end")
def end_session(session_id: int, db: Session = Depends(get_db)):
    session = db.query(StudySession).filter(StudySession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if session.end_time is not None:
        raise HTTPException(status_code=400, detail="Session already ended")
    session.end_time = datetime.utcnow()
    db.commit()
    db.refresh(session)
    return {"message": "Session ended", "session_id": session.id}
