from fastapi import HTTPException
from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from database.models import DBPost
import datetime

def create(db: Session, post: PostBase):
    db_post = DBPost(
        title=post.title,
        content=post.content,
        image_url=post.image_url,
        author=post.author,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_all(db: Session):
    return db.query(DBPost).all()

def delete(db: Session, post_id: int):
    post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if not post:
        return HTTPException(status_code=404, detail="Post not found")    
    db.delete(post)
    db.commit()
    return True
    

