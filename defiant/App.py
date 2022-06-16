from fastapi import FastAPI
import redis
from models import Post

db = {}



# r = redis.from_url("redis://default:redispw@localhost:49160" ,decode_responses=True)

app = FastAPI()

@app.post("/post")
async def create_post(post: Post):
    posts.append(post)
    return post.id

@app.get("/posts/")
async def get_posts():
    return posts


@app.get("/post/{id}")
async def get_post(id: str):
    post = [post for post in posts if post.id == id]
    print(post)
    return post

@app.put("/post/{id}")
async def update_post(id:str, new_post: Post):
    post = [post for post in posts if post.id == id]
    posts.append(new_post)
    return new_post.id


app.delete("/post/")