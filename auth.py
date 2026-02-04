from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, utils, oauth2
from app.database import get_db

router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=schemas.Token)
def login(credentials: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == credentials.email).first()
    
    if not user or not utils.verify_password(credentials.password, user.password):
        raise HTTPException(status_code=403, detail="Invalid credentials")

    token = oauth2.create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}
