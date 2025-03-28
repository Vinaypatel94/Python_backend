from sqlalchemy import Column, Integer,String,Boolean
from database import Base


class Todo(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column( String, nullable=False, index=True)
    description = Column (String, nullable=False, index=True)
    completed = Column(Boolean, nullable=False, default=0, index=True)



