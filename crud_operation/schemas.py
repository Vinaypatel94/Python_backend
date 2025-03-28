from pydantic import BaseModel

# Pydantic schema for user input and response


class UserSchema(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True  # Tells Pydantic to treat SQLAlchemy models as dictionaries


class UpdateUserSchema(BaseModel):
    name: str = None
    email: str = None
    password: str = None

    class Config:
        orm_mode = True
