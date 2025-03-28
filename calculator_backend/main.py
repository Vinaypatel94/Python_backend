from fastapi import FastAPI, Depends,HTTPException
from pydantic import BaseModel
from database import Base, engine, SessionLocal
from models import Calculation
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/calculate/")
def calculate(operation: str, num1: float, num2: float, db: Session = Depends(get_db)):

    if operation == "add":
        result = num1+num2
    elif operation == "subtract":
        result = num1-num2
    elif operation == "multiply":
        result = num1*num2
    elif operation == "divide":
        if num2==0:
            raise HTTPException(status_code=400,detail="can not divide by zero")
        result=num1/num2
    else:
        raise HTTPException(status_code=400,detail="invalid operation")


    calc = Calculation(operation=operation, num1=num1, num2=num2, result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    return {"id": calc.id, "operation": operation, "num1": num1, "num2": num2, "result": result}
