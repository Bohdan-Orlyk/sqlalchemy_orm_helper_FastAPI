from pydantic import BaseModel
from api.books_examples.schemas.book_scheme import BookScheme


class BaseAuthorScheme(BaseModel):
    author_name: str


class ReadAuthorScheme(BaseAuthorScheme):
    author_id: int

    books: list[BookScheme]


class CreateAuthorScheme(BaseAuthorScheme):
    pass



