from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def ping():
    return "pong"


@app.post("/colegio")
def read_item():
    return {"item_id": item_id, "q": q}