from pydantic import BaseModel, Field
from .MongoId import PyObjectId


class Post(BaseModel):
    """Model to store posts"""

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    body: str = Field(...)
    author: str = Field(...)
    tags: list[str] = Field(...)

    class Config:
        allow_population_by_field_name = True
