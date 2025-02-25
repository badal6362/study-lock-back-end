from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine

app = FastAPI()

# Configure CORS to allow requests from your frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create all database tables.
Base.metadata.create_all(bind=engine)

# Include existing routers (authentication, study sessions, goals, etc.)
from auth import register, login
app.include_router(register.router, prefix="/auth")
app.include_router(login.router, prefix="/auth")

from study_sessions import start_session, end_session, history
app.include_router(start_session.router, prefix="/study-sessions")
app.include_router(end_session.router, prefix="/study-sessions")
app.include_router(history.router, prefix="/study-sessions")

from goals import set_goal, update_goal, get_goal
app.include_router(set_goal.router, prefix="/goals")
app.include_router(update_goal.router, prefix="/goals")
app.include_router(get_goal.router, prefix="/goals")

# Include leaderboard endpoints.
from Leaderboard import update_leaderboard, get_leaderboard
app.include_router(update_leaderboard.router, prefix="/leaderboard")
app.include_router(get_leaderboard.router, prefix="/leaderboard")

@app.get("/")
def root():
    return {"message": "StudyLock Backend is Running"}
