from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


# ─── Contact ─────────────────────────────────────────────────────
class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    source: Optional[str] = None
    message: Optional[str] = None


class ContactUpdate(BaseModel):
    status: Optional[str] = None


class ContactOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    source: Optional[str] = None
    message: Optional[str] = None
    status: str
    created_at: Optional[datetime] = None


# ─── Subscriber ──────────────────────────────────────────────────
class SubscriberCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str


class SubscriberOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    is_active: bool
    created_at: Optional[datetime] = None
