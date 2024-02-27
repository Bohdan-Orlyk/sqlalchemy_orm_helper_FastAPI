from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from api.books_examples.models.author_model import Author


class CRUDService:

    @staticmethod
    async def get_authors_with_books(session: AsyncSession):
        stmt = select(Author).options(joinedload(Author.books)).order_by(Author.author_id)

        result = await session.scalars(stmt)
        authors = result.unique().all()

        return authors
