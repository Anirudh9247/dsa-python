from fastapi import FastAPI

app = FastAPI() #application instance

@app.get("/") #decorator
def read_root():
    return {"message": "Backend journey started"}
@app.get("/hello/{name}") #path parameter
def say_hello(name: str):
    return {"message": f"Hello {name}"}
@app.get("/square")
def square(number : int):
    return{"result ": number * number}