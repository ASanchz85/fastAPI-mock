import os
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor


app = FastAPI()
load_dotenv()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


try:
    connection = psycopg2.connect(
        user=os.getenv("USER_DB"),
        password=os.getenv("PASSWORD_DB"),
        host=os.getenv("DATABASE_URL"),
        database=os.getenv("DATABASE_NAME"),
        port=os.getenv("DATABASE_PORT"),
        cursor_factory=RealDictCursor,
    )

    cursor = connection.cursor()
    print("Connection to PostgreSQL DB successful")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)


my_posts = [
    {
        "title": "Example by default",
        "content": "Just here to test API functionality",
        "published": True,
        "rating": 5,
        "id": 1,
    },
    {
        "title": "second post as an example",
        "content": "another simple post to test the API",
        "published": True,
        "rating": 3,
        "id": 2,
    },
]


@app.get("/")
async def root():
    return {
        "message": "welcome to our API, visit the link below to get access to the documentation",
        "docs_link": "http://localhost:8000/docs",
        "error": None,
    }


@app.get("/posts")
async def get_posts():
    return {"message": "Successfully requested", "data": my_posts, "error": None}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(new_post: Post):
    # !deprecated >> my_posts.append(new_post.dict())
    post_dict = new_post.__dict__
    post_dict["id"] = randrange(0, 100000)
    my_posts.append(post_dict)

    # ?? note that you don't need to type each response.status_code, you can just use the status code as a parameter
    # response.status_code = status.HTTP_201_CREATED
    return {"message": "Successfully created post", "data": post_dict, "error": None}


# !carefull with the order of the routes, because the one with the variable can't be the first one
@app.get("/posts/latest", status_code=status.HTTP_200_OK)
async def get_latest_post():
    latest_post = my_posts[-1]
    return {"message": "Successfully requested", "data": latest_post, "error": None}


@app.get("/posts/{post_id}")
async def get_single_post(post_id: int):
    for post in my_posts:
        if post["id"] == post_id:
            return {"message": "Successfully requested", "data": post, "error": None}

    raise HTTPException(status_code=404, detail="Post not found")
    # return {"message": "Post not found", "data": None, "error": "Post not found"}


@app.delete("/posts/{post_id}")
async def delete_post(post_id: int, status_code=status.HTTP_204_NO_CONTENT):
    for post in my_posts:
        if post["id"] == post_id:
            my_posts.remove(post)

            # ?? when using 204 status code, you don't need to return any data
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail="Post not found")


@app.put("/posts/{post_id}")
async def update_post(post_id: int, updated_post: Post):
    for post in my_posts:
        if post["id"] == post_id:
            post["title"] = updated_post.title
            post["content"] = updated_post.content
            post["published"] = updated_post.published
            post["rating"] = (
                updated_post.rating if updated_post.rating else post["rating"]
            )

            return {"message": "Successfully updated post", "data": post, "error": None}

    raise HTTPException(status_code=404, detail="Post not found")
