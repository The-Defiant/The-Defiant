from pydantic import BaseModel


class Post(BaseModel):
    """Model to store posts"""
    id: int
    title: str
    body: str
    author: str
    tags: list[str]
