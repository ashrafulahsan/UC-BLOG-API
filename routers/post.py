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

@router.delete("/delete/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    result = db_post.delete(db, post_id)
    if result is True:
        return {"message": "Post deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")