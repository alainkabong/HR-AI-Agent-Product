from sqlalchemy import Boolean, Column, Integer, String, Text
from app.core.database import Base 

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    requirements = Column(Text, nullable=False)
    location = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    

    
    
    
    