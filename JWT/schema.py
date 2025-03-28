from pydantic import BaseModel, EmailStr

# Pydantic models


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    phone_no: int
    email_id: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    phone_no: int
    email_id: str
    username: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
