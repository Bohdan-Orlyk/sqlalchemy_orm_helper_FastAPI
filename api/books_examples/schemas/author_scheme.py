from pydantic import BaseModel
from api.books_examples.schemas.book_scheme import BookScheme


class AuthorScheme(BaseModel):
    author_name: str

    books: list[BookScheme]
