from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas, oauth2
from app.database import get_db

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=list[schemas.PostOut])
def get_posts(db: Session = Depends(get_db)):
    posts = (
        db.query(
            models.Post,
            func.count(models.Vote.post_id).label("votes")
        )
        .outerjoin(models.Vote, models.Vote.post_id == models.Post.id)
        .group_by(models.Post.id)
        .all()
    )
    return [{"votes": v, **p.__dict__} for p, v in posts]

@router.post("/", response_model=schemas.PostOut)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user)
):
    new_post = models.Post(owner_id=user_id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {**new_post.__dict__, "votes": 0}
