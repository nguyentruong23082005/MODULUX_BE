from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, func
from app.db.session import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    source = Column(String, nullable=True)
    message = Column(Text, nullable=True)
    status = Column(String, default="new")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    delete_at = Column(DateTime(timezone=True), nullable=True)
    delete_by = Column(Integer, nullable=True)


class Subscriber(Base):
    __tablename__ = "subscribers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    delete_at = Column(DateTime(timezone=True), nullable=True)
    delete_by = Column(Integer, nullable=True)
