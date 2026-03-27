from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey, func
from app.db.session import Base


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    title = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False, index=True)
    content = Column(Text, nullable=True)
    meta_title = Column(String, nullable=True)
    meta_description = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    delete_at = Column(DateTime(timezone=True), nullable=True)
    delete_by = Column(Integer, nullable=True)


class Faq(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question = Column(String, nullable=False)
    answer = Column(Text, nullable=False)
    display_order = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
    delete_at = Column(DateTime(timezone=True), nullable=True)
    delete_by = Column(Integer, nullable=True)
