from pydantic import BaseModel


class BookScheme(BaseModel):
    title: str


