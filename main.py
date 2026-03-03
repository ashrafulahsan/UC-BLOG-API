from fastapi import FastAPI
from database import models
from database.database import engine
from routers import post

app = FastAPI()
app.include_router(post.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


models.Base.metadata.create_all(bind=engine)
