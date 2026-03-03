from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    image_url: str | None = None
    author: str

class PostResponse(PostBase):
    id: int
    title: str
    content: str
    image_url: str | None = None
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True
