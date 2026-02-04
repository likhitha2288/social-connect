from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, oauth2
from app.database import get_db

router = APIRouter(prefix="/vote", tags=["Votes"])

@router.post("/")
def vote(
    vote: schemas.Vote,
    db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user)
):
    existing = db.query(models.Vote).filter_by(
        post_id=vote.post_id, user_id=user_id
    ).first()

    if vote.dir == 1:
        if existing:
            raise HTTPException(status_code=409, detail="Already voted")
        db.add(models.Vote(post_id=vote.post_id, user_id=user_id))
    else:
        if not existing:
            raise HTTPException(status_code=404, detail="Vote not found")
        db.delete(existing)

    db.commit()
    return {"message": "Success"}
