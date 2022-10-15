from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    date: str



@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/picture")
async def main():
    return {"date":"1999", "img_src":"https://www.princeton.edu/sites/default/files/styles/half_1x/public/images/2022/02/KOA_Nassau_2697x1517.jpg?itok=fAtaOLnw"}

@app.post("/date")
async def create_item(item: Item):
    return item


