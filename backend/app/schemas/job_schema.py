from typing import Optional
from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    description: str      
    requirements: str
    location: Optional[str] = None
    
    
class JobResponse(BaseModel):
    id: int
    title: str  
    description: str 
    requirements: str 
    location: Optional[str] = None
    is_active: bool 
    
    class Config:
        from_attributes = True
        