from pydantic import BaseModel, Field


class UserData(BaseModel):
    username: str = Field(..., min_length=8, max_length=20)
    password: str = Field(..., min_length=8, max_length=20)



class Note(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    text: str = Field(..., min_length=1, max_length=300)


class User(BaseModel):
    user_id: int


class Token(BaseModel):
    access_token: str
    token_type: str