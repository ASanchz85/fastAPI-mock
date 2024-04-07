from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "title": "Example by default",
        "content": "Just here to test API functionality",
        "published": True,
        "rating": 5,
        "id": 1
    },
    {
        "title": "second post as an example",
        "content": "another simple post to test the API",
        "published": True,
        "rating": 3,
        "id": 2
    }
]


@app.get("/")
async def root():
    return {"message": "welcome to our API, visit the link below to get access to the documentation", "docs_link": "http://localhost:8000/docs", "error": None}

    
@app.get("/posts")
async def get_posts():
    return {"message": "Successfully requested", "data": my_posts, "error": None}


@app.post("/posts")
async def create_post(new_post: Post):
    # !deprecated >> my_posts.append(new_post.dict())
    post_dict = new_post.__dict__
    post_dict["id"] = randrange(0, 100000)
    my_posts.append(post_dict)
    print(my_posts)
    return {"message": "Successfully created post", "data": post_dict, "error": None}


# !carefull with the order of the routes, because the one with the variable can't be the first one
@app.get("/posts/latest")
async def get_latest_post():
    latest_post = my_posts[-1]
    return {"message": "Successfully requested", "data": latest_post, "error": None}


@app.get("/posts/{post_id}")
async def get_single_post(post_id: int):
    for post in my_posts:
        if post["id"] == post_id:
            return {"message": "Successfully requested", "data": post, "error": None}
    return {"message": "Post not found", "data": None, "error": "Post not found"}