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
    }
]


@app.get("/")
async def root():
    return {"message": "Successfully requested", "data": my_posts, "error": None}


@app.post("/posts")
async def create_post(new_post: Post):
    # !deprecated >> my_posts.append(new_post.dict())
    post_dict = new_post.__dict__
    post_dict["id"] = randrange(0, 100000)
    my_posts.append(post_dict)
    print(my_posts)
    return {"message": "Successfully created post", "data": post_dict, "error": None}
