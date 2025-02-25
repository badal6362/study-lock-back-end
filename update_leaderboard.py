from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Leaderboard

router = APIRouter()

class LeaderboardUpdateRequest(BaseModel):
    user_id: str
    total_study_minutes: int

@router.post("/update")
def update_leaderboard(req: LeaderboardUpdateRequest, db: Session = Depends(get_db)):
    # Check if the leaderboard entry exists for the given user_id.
    leaderboard_entry = db.query(Leaderboard).filter(Leaderboard.user_id == req.user_id).first()
    if not leaderboard_entry:
        # Create a new entry if it doesn't exist.
        leaderboard_entry = Leaderboard(user_id=req.user_id, total_study_minutes=req.total_study_minutes)
        db.add(leaderboard_entry)
    else:
        # Otherwise, update the existing entry.
        leaderboard_entry.total_study_minutes = req.total_study_minutes
    db.commit()
    db.refresh(leaderboard_entry)
    return {
        "message": "Leaderboard updated",
        "data": {
            "user_id": leaderboard_entry.user_id,
            "total_study_minutes": leaderboard_entry.total_study_minutes
        }
    }
