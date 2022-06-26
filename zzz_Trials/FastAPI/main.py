from fastapi import FastAPI
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


app = FastAPI()


@app.get("/")
def root():
    return {"Mesage": "Hello World from Basic Fast API"}


# Passing Parameters
@app.get("/items/{some_item}")
async def read_item(some_item: str):
    return {"Recieved Item": some_item}


@app.get("/fixed-items/{fixed_items}")
async def read_defined_items(fixed_items: Gender):
    return {"Fixed Item List: ": fixed_items}
