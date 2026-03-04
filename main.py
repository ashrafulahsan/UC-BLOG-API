from fastapi import FastAPI
from database import models
from database.database import engine
from routers import post
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(post.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


models.Base.metadata.create_all(bind=engine)

app.mount("/images", StaticFiles(directory="images"), name="images")


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)   