from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db import Base, engine, SessionLocal
from schemas import UserSchema, UpdateUserSchema
from models import User
from crud import create_user, get_users, get_user_by_id, update_user, delete_user
from typing import List

# Initialize FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the DB session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create User


@app.post("/users", response_model=UserSchema)
def create_user_route(user: UserSchema, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

# Get all Users


@app.get("/users", response_model=List[UserSchema])
def get_users_route(db: Session = Depends(get_db)):
    return get_users(db=db)

# Get User by ID


@app.get("/users/{user_id}", response_model=UserSchema)
def get_user_route(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update User


@app.put("/users/{user_id}", response_model=UserSchema)
def update_user_route(user_id: int, updates: UpdateUserSchema, db: Session = Depends(get_db)):
    return update_user(db=db, user_id=user_id, updates=updates)

# Delete User


@app.delete("/users/{user_id}", response_model=UserSchema)
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db=db, user_id=user_id)
