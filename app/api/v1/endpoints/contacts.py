from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.api.deps import get_current_user
from app.schemas.contact import ContactCreate, ContactUpdate, ContactOut
from app.crud.crud_contact import get_contacts, get_contact, create_contact, update_contact, soft_delete_contact
from app.models.user import User

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.get("/", response_model=List[ContactOut])
def list_contacts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    """Admin only: liệt kê tất cả liên hệ."""
    return get_contacts(db, skip=skip, limit=limit)


@router.get("/{contact_id}", response_model=ContactOut)
def get_one(contact_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    obj = get_contact(db, contact_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Contact not found")
    return obj


@router.post("/", response_model=ContactOut, status_code=201)
def create(data: ContactCreate, db: Session = Depends(get_db)):
    """Public: gửi form liên hệ."""
    return create_contact(db, data)


@router.put("/{contact_id}", response_model=ContactOut)
def update_status(contact_id: int, data: ContactUpdate, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    obj = update_contact(db, contact_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Contact not found")
    return obj


@router.delete("/{contact_id}", status_code=204)
def delete(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    obj = get_contact(db, contact_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Contact not found")
    soft_delete_contact(db, contact_id, deleted_by=current_user.id)
