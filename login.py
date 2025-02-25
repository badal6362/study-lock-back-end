from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import User

router = APIRouter()

# Pydantic model for the login request.
class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login_user(user: LoginRequest, db: Session = Depends(get_db)):
    # Retrieve the user based on the provided email.
    db_user = db.query(User).filter(User.email == user.email).first()
    
    # Validate the password.
    if not db_user or db_user.hashed_password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful", "user_id": db_user.id}
