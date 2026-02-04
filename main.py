from fastapi import FastAPI
from app import models
from app.database import Base, engine
from app.routers import auth, users, posts, votes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Social Connect Backend API")
@app.get("/")
def root():
    return {"message": "Social Connect API is running"}

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(votes.router)
