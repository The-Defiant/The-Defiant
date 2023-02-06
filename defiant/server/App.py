import re
from fastapi import FastAPI
from .database import post_db, post_collection

from .models import Post


app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to defiant blog"}


@app.get("/post/{post_id}", tags=["Posts"])
async def get_post(post_id: int):
    return post_collection.find_one({"id": post_id})


@app.post("/post", tags=["Posts"])
async def send_post(post: Post):
    print(post)
    return post_collection.insert_one(post.dict()).inserted_id
