from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Leaderboard

router = APIRouter()

@router.get("/top")
def get_leaderboard(db: Session = Depends(get_db)):
    # Retrieve all leaderboard entries sorted by total_study_minutes in descending order.
    leaderboard = db.query(Leaderboard).order_by(Leaderboard.total_study_minutes.desc()).all()
    # Convert the entries to a list of dictionaries for a cleaner response.
    result = [
        {"user_id": entry.user_id, "total_study_minutes": entry.total_study_minutes}
        for entry in leaderboard
    ]
    return result
