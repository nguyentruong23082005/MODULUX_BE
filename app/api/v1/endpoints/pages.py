from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.api.deps import get_current_user
from app.schemas.page import PageCreate, PageUpdate, PageOut
from app.crud.crud_page import get_pages, get_page, get_page_by_slug, create_page, update_page, soft_delete_page
from app.models.user import User

router = APIRouter(prefix="/pages", tags=["Pages"])


@router.get("/", response_model=List[PageOut])
def list_pages(db: Session = Depends(get_db)):
    return get_pages(db)


@router.get("/slug/{slug}", response_model=PageOut)
def get_by_slug(slug: str, db: Session = Depends(get_db)):
    obj = get_page_by_slug(db, slug)
    if not obj:
        raise HTTPException(status_code=404, detail="Page not found")
    return obj


@router.get("/{page_id}", response_model=PageOut)
def get_one(page_id: int, db: Session = Depends(get_db)):
    obj = get_page(db, page_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Page not found")
    return obj


@router.post("/", response_model=PageOut, status_code=201)
def create(data: PageCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_page(db, data, author_id=current_user.id)


@router.put("/{page_id}", response_model=PageOut)
def update(page_id: int, data: PageUpdate, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    obj = update_page(db, page_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Page not found")
    return obj


@router.delete("/{page_id}", status_code=204)
def delete(page_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    obj = get_page(db, page_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Page not found")
    soft_delete_page(db, page_id, deleted_by=current_user.id)
