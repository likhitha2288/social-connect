from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        from_attributes = True

class Login(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    owner_id: int
    votes: int
    class Config:
        from_attributes = True

class Vote(BaseModel):
    post_id: int
    dir: int  # 1 = vote, 0 = remove
