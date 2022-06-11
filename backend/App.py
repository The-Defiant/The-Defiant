from enum import Enum
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hellow world"}


# routes regarding user authentication

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
    
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name, "object": ModelName.__dict__[model_name]}   



fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
    
    
app.post("/items/")
async def create_item(item: Item):
    return item