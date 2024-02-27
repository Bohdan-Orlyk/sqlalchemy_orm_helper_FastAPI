from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from api.books_examples.models.author_model import Author
from api.books_examples.schemas.author_scheme import CreateAuthorScheme


class CRUDService:

    @staticmethod
    async def get_all_authors_with_all_books(session: AsyncSession):
        stmt = select(Author).options(joinedload(Author.books)).order_by(Author.author_id)

        result = await session.scalars(stmt)
        authors = result.unique().all()

        return authors

    @staticmethod
    async def get_only_authors_with_books(session: AsyncSession):
        stmt = (
            select(Author)
            .join(Author.books)
            .options(joinedload(Author.books))
            .order_by(Author.author_id)
        )

        result = await session.scalars(stmt)
        authors = result.unique().all()

        return authors

    @staticmethod
    async def get_author_by_id(session: AsyncSession, author_id: int):
        author_by_id = await session.get(Author, author_id)

        if author_by_id:
            stmt = (
                select(Author)
                .options(joinedload(Author.books))
                .where(Author.author_id == author_id)
            )

            author_with_books = await session.execute(stmt)

            return author_with_books.scalar()
        return None

    @staticmethod
    async def create_author(session: AsyncSession, author_scheme: CreateAuthorScheme) -> Author:
        author = Author(**author_scheme.model_dump())

        session.add(author)
        await session.commit()
        await session.refresh(author)

        return author
