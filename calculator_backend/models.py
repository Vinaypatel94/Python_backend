from sqlalchemy import Column,Integer,String,Float
from database import Base


class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    num1 = Column(Float, index=True, nullable=False)
    num2 = Column(Float, index=True, nullable=False)
    result = Column(Float, index=True)