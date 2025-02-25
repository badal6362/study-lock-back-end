from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import uuid
from database import get_db
from models import Goal

router = APIRouter()

class GoalRequest(BaseModel):
    title: str
    description: str

@router.post("/set")
def set_goal(user_id: str, goal: GoalRequest, db: Session = Depends(get_db)):
    new_goal = Goal(
        user_id=user_id,
        title=goal.title,
        description=goal.description
    )
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return {"message": "Goal set", "goal_id": new_goal.id}
