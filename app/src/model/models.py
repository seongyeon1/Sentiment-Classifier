from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(255), index=True)  # Specify length for VARCHAR
    label = Column(String(50))              # Specify length for VARCHAR
    score = Column(Float)
