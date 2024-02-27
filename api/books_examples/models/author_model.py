from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base_model import Base
from api.books_examples.models.book_model import Book


class Author(Base):
    __tablename__ = "author"

    author_id: Mapped[int] = mapped_column(primary_key=True)
    author_name: Mapped[str]

    books: Mapped[list["Book"]] = relationship("Book")

