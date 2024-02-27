from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from database.base_model import Base


class Book(Base):
    __tablename__ = "book"

    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]

    author_id: Mapped[int] = mapped_column(ForeignKey("author.author_id"))



