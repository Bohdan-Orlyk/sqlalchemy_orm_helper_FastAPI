import uvicorn
import asyncio

from fastapi import FastAPI, status
from database.db_helper import database_helper

from api.books_examples.router import books_router

app = FastAPI()

ROUTERS = [
    books_router,
]


@app.get("/")
def get_ok():

    return {
        "status": status.HTTP_200_OK,
        "message": "OK"
    }


if __name__ == "__main__":
    asyncio.run(database_helper.create_tables())

    [app.include_router(router) for router in ROUTERS]

    uvicorn.run(app=app, host="localhost", port=9876)

