from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.books_examples.schemas.author_scheme import AuthorScheme
from database.db_helper import database_helper
from services.crud_services import CRUDService

books_router = APIRouter(prefix="/books", tags=["Books"])


@books_router.get("/", response_model=list[AuthorScheme])
async def read_all(session: AsyncSession = Depends(database_helper.get_session),
                   crud_service: CRUDService = Depends(CRUDService)) -> list[AuthorScheme]:

    authors = await crud_service.get_authors_with_books(session=session)

    return authors
