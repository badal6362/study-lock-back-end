from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database URL; the database file "studylock.db" will be created in your project folder.
DATABASE_URL = "sqlite:///./studylock.db"

# Create the SQLAlchemy engine.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models.
Base = declarative_base()

# Dependency: provides a new database session for each request.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
