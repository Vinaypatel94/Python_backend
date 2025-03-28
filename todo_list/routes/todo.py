from fastapi import APIRouter, Depends, HTTPException
from schemas import TodoResponse,TodoCreate
from sqlalchemy.orm import Session
from database import get_db
from crud import create_todo, delete_todo, update_todo, get_todo,get_todos

router =APIRouter()

@router.post("/",response_model=TodoResponse)
def create(todo: TodoCreate, db: Session=Depends(get_db)):
    return create_todo(db,todo)

@router.get("/",response_model=list[TodoResponse])
def read_all(db: Session = Depends(get_db)):
    return get_todos(db)

@router.get("/{todo_id}",response_model=TodoResponse)
def read_one(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if todo is None:
        raise HTTPException (status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoResponse)
def update(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    return update_todo(db, todo_id, todo)

@router.delete("/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    delete = delete_todo(db,todo_id)
    if delete is None:
        raise HTTPException(status_code=400, detail="Todo not found")
    return {"message":"Deleted successfully"}