from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from routers.schemas import PostBase, PostResponse
from database import db_post

router = APIRouter(
    prefix="/posts", 
    tags=["Posts"]
)

@router.post("/", response_model=PostResponse)
def create_post(post: PostBase, db: Session = Depends(get_db)):
    new_post = db_post.create(db, post)
    return new_post