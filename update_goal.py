from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Goal

router = APIRouter()

class GoalUpdateRequest(BaseModel):
    title: str = None
    description: str = None

@router.patch("/update")
def update_goal(goal_id: str, goal_update: GoalUpdateRequest, db: Session = Depends(get_db)):
    goal = db.query(Goal).filter(Goal.id == goal_id).first()
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    if goal_update.title:
        goal.title = goal_update.title
    if goal_update.description:
        goal.description = goal_update.description
    db.commit()
    db.refresh(goal)
    return {"message": "Goal updated", "goal_id": goal.id}
