from sqlalchemy import Column, DateTime, func, Integer
from ..db.sessions import Base



class BaseModel(Base):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())