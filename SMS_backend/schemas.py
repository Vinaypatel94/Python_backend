from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, time, datetime


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class PermissionSchema(BaseModel):
    id: Optional[int]
    name: str


class RoleSchema(BaseModel):
    id: Optional[int]
    name: str
    permissions: List[PermissionSchema] = []


class UserCreate(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    email: EmailStr
    phone_no: int
    username: str
    password: str
    role: List[str] = []


class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    phone_no: int
    email: str
    username: str
    roles: list[RoleSchema]


# create attendence pydantic schema
class AttendanceCreate(BaseModel):
    user_id: int
    date: date
    check_in: Optional[time] = None
    check_out: Optional[time] = None
    total_hours: Optional[float] = None
    overtime_hours: Optional[float] = None
    status: str


class AttendanceResponse(AttendanceCreate):
    id: int

    class Config:
        from_attributes = True


class AttendanceUpdate(BaseModel):
    check_in: Optional[time] = None
    check_out: Optional[time] = None
    total_hours: Optional[float] = None
    overtime_hours: Optional[float] = None
    status: Optional[str] = None


# create leave schema
class LeaveRecordCreate(BaseModel):
    user_id: int
    leave_type: str
    start_date: date
    end_date: date
    # status: str


class LeaveRecordResponse(LeaveRecordCreate):
    id: int

    class config:
        from_attributes = True


class LeaveRecordUpdate(BaseModel):
    leave_type: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None
