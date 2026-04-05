from datetime import date

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class AuthorsList(AuthorBase):
    id: int
    books: "BooksList"

    class Config:
        from_attributes = True


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date


class BookCreate(BookBase):
    author_id: int


class BooksList(BookBase):
    id: int
    authors: AuthorsList

    class Config:
        from_attributes = True
