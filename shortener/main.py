from fastapi import FastAPI, Depends, HTTPException
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import shortuuid
from models import URL

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten/")
def shorten_url(long_url: str, db: Session = Depends(get_db)):
    short_code = shortuuid.ShortUUID().random(length=6)
    new_url = URL(short_code=short_code, long_url=long_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return {"short_url": f"http://localhost:8000/{short_code}"} 


@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == short_code).first()
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"redirect_to": url.long_url}

