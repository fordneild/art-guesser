from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import uvicorn
from views import object_router

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


@app.post("/date")
async def date(item: date):
    real_date = 1999
    guessed_date = item.date
    remainder = real_date - guessed_date
    content = jsonable_encoder({"remainder": remainder, "date": real_date})
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


app.include_router(object_router)


class Server:
    app = "main:app"

    def runServer(self, host: str, port: int, is_dev: bool):
        uvicorn.run(self.app, host=host, port=port, debug=is_dev)


if __name__ == "__main__":
    server = Server()
    host = "0.0.0.0"
    port = 8000
    is_dev = True
    server.runServer(host, port, is_dev)
