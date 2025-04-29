from pydantic import BaseModel, EmailStr, UUID4
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class GetUser(BaseModel):
    name: str
    email: EmailStr
    created_at: datetime
    
class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True