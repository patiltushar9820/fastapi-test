from fastapi import FastAPI, Form
from typing import Annotated
from app.routers.functions import *
# from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test():
    data = test()
    return {"message": data}

@app.put("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}