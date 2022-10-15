from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class date(BaseModel):
    date: int


class artist(BaseModel):
    artist: str


class style(BaseModel):
    style: str


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get("/picture")
async def main():
    return {
        "date": "1999",
        "img_src": "https://www.princeton.edu/sites/default/files/styles/half_1x/public/images/2022/02/KOA_Nassau_2697x1517.jpg?itok=fAtaOLnw",
    }


@app.post("/date")
async def date(item: date):
    real_date = 1999
    guessed_date = item.date
    remainder = real_date - guessed_date
    content = jsonable_encoder({"remainder": remainder})
    return JSONResponse(content=content)


@app.post("/artist")
async def artist(item: artist):
    real_artist = "Ford"
    content = jsonable_encoder({"artist": real_artist})
    return JSONResponse(content=content)


@app.post("/style")
async def style(item: style):
    real_style = "cool"
    content = jsonable_encoder({"style": real_style})
    return JSONResponse(content=content)
