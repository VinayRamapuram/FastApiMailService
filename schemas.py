from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    email: str
    password: str
    name: str


class ShowUser(BaseModel):
    email: str
    name: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None