from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Goal

router = APIRouter()

@router.get("/")
def get_goals(user_id: str, db: Session = Depends(get_db)):
    goals = db.query(Goal).filter(Goal.user_id == user_id).all()
    return goals
