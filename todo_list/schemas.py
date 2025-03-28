from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool 

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(TodoCreate):
    
    id: int

    class config:
        from_attributes = True