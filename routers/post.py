from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from routers.schemas import PostBase, PostResponse
from database import db_post

router = APIRouter(
    prefix="/posts", 
    tags=["Posts"]
)

@router.post("/create", response_model=PostResponse)
def create_post(post: PostBase, db: Session = Depends(get_db)):
    new_post = db_post.create(db, post)
    return new_post

@router.get("/all", response_model=list[PostResponse])
def get_all_posts(db: Session = Depends(get_db)):
    posts = db_post.get_all(db)
    return posts