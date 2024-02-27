from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from api.books_examples.schemas.author_scheme import ReadAuthorScheme, CreateAuthorScheme
from database.db_helper import database_helper
from services.crud_services import CRUDService

books_router = APIRouter(prefix="/books", tags=["Books"])


@books_router.get("/", response_model=list[ReadAuthorScheme])
async def read_all_authors(session: AsyncSession = Depends(database_helper.get_session),
                           crud_service: CRUDService = Depends(CRUDService)) -> list[ReadAuthorScheme]:
    authors = await crud_service.get_all_authors_with_all_books(session=session)

    return authors


@books_router.get("/only_authors_with_books", response_model=list[ReadAuthorScheme])
async def read_only_authors_with_books(session: AsyncSession = Depends(database_helper.get_session),
                                       crud_service: CRUDService = Depends(CRUDService)):

    authors_with_books = await crud_service.get_only_authors_with_books(session=session)

    return authors_with_books


@books_router.get("/{author_id}/", response_model=ReadAuthorScheme)
async def read_author_by_id(author_id: int,
                            session: AsyncSession = Depends(database_helper.get_session),
                            crud_service: CRUDService = Depends(CRUDService)):
    try:
        author_by_id = await crud_service.get_author_by_id(session=session, author_id=author_id)
        if not author_by_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return author_by_id

    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@books_router.post("/", status_code=status.HTTP_201_CREATED, response_model=CreateAuthorScheme)
async def create_author(author_scheme: CreateAuthorScheme,
                        session: AsyncSession = Depends(database_helper.get_session),
                        crud_service: CRUDService = Depends(CRUDService)):
    try:
        created_author = await crud_service.create_author(session=session, author_scheme=author_scheme)

        return created_author
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
