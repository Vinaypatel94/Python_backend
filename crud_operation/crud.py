from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema, UpdateUserSchema
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError


# Create a new user
def create_user(db: Session, user: UserSchema):
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already exists")

        new_user = User(name=user.name, email=user.email, password=user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    except SQLALchemy as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"error creating user:{str(e)}")


# Get all users
def get_users(db: Session):
    return db.query(User).all()


# Get a specific user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# Update a user's details
def update_user(db: Session, user_id: int, updates: UpdateUserSchema):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating user: {str(e)}")

# Delete a user
def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        db.delete(user)
        db.commit()
        return user
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting user:{str(e)}")
v