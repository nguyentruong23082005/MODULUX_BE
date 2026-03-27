from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.models.contact import Contact, Subscriber
from app.schemas.contact import ContactCreate, ContactUpdate, SubscriberCreate

_now = lambda: datetime.now(timezone.utc)


# ─── Contact ─────────────────────────────────────────────────────
def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Contact).filter(Contact.delete_at == None).offset(skip).limit(limit).all()


def get_contact(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id, Contact.delete_at == None).first()


def create_contact(db: Session, data: ContactCreate):
    obj = Contact(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_contact(db: Session, contact_id: int, data: ContactUpdate):
    obj = get_contact(db, contact_id)
    if obj:
        for k, v in data.model_dump(exclude_none=True).items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj


def soft_delete_contact(db: Session, contact_id: int, deleted_by: int):
    obj = get_contact(db, contact_id)
    if obj:
        obj.delete_at = _now()
        obj.delete_by = deleted_by
        db.commit()
    return obj


# ─── Subscriber ──────────────────────────────────────────────────
def get_subscribers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Subscriber).filter(Subscriber.delete_at == None).offset(skip).limit(limit).all()


def get_subscriber(db: Session, subscriber_id: int):
    return db.query(Subscriber).filter(Subscriber.id == subscriber_id, Subscriber.delete_at == None).first()


def get_subscriber_by_email(db: Session, email: str):
    return db.query(Subscriber).filter(Subscriber.email == email, Subscriber.delete_at == None).first()


def create_subscriber(db: Session, data: SubscriberCreate):
    obj = Subscriber(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def soft_delete_subscriber(db: Session, subscriber_id: int, deleted_by: int):
    obj = get_subscriber(db, subscriber_id)
    if obj:
        obj.delete_at = _now()
        obj.delete_by = deleted_by
        db.commit()
    return obj
