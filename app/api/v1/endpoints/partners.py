from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.api.deps import get_current_user
from app.schemas.site import PartnerCreate, PartnerUpdate, PartnerOut
from app.crud.crud_site import get_partners, get_partner, create_partner, update_partner, soft_delete_partner
from app.models.user import User

router = APIRouter(prefix="/partners", tags=["Partners"])


@router.get("/", response_model=List[PartnerOut])
def list_partners(db: Session = Depends(get_db)):
    return get_partners(db)


@router.get("/{partner_id}", response_model=PartnerOut)
def get_one(partner_id: int, db: Session = Depends(get_db)):
    obj = get_partner(db, partner_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Partner not found")
    return obj


@router.post("/", response_model=PartnerOut, status_code=201)
def create(data: PartnerCreate, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    return create_partner(db, data)


@router.put("/{partner_id}", response_model=PartnerOut)
def update(partner_id: int, data: PartnerUpdate, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    obj = update_partner(db, partner_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Partner not found")
    return obj


@router.delete("/{partner_id}", status_code=204)
def delete(partner_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    obj = get_partner(db, partner_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Partner not found")
    soft_delete_partner(db, partner_id, deleted_by=current_user.id)
