from sqlalchemy.orm import Session
from schemas import TodoCreate,TodoUpdate
from models import Todo

def create_todo(db: Session, todo: TodoCreate):
    if not todo.title or not todo.description:
        raise ValueError("title and description is not empty")

    db_todo = Todo(title=todo.title, description=todo.description, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todos(db: Session):

    return db.query(Todo).all()

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id==todo_id).first()

def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    db_todo = db.query(Todo).filter(Todo.id==todo_id).first()
    if db_todo:
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.completed = todo.completed
        db.commit()
        db.refresh(db_todo)
        return db_todo
  
def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todo).filter(Todo.id==todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return db_todo 
