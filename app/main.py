from fastapi import FastAPI
from requests import request

from app.database import database
from .routers import account, teams

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(account.router)
app.include_router(teams.router)
