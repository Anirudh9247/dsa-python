from fastapi import FastAPI
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    price: float

app = FastAPI() #application instance

@app.get("/") #decorator
def read_root():
    return {"message": "Backend journey started"}

@app.get("/hello/{name}") #path parameter
def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/square") #query parameter
def square(number : int):
    return{"result ": number * number}

@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item received",
        "item": item
    }

