from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import CORS_ORIGINS
from app.db.session import engine, Base
from app.api.v1.api import api_router

# Import tất cả models để SQLAlchemy nhận diện khi tạo bảng
from app.models import (  # noqa: F401
    user, site, project, blog, page, contact
)

app = FastAPI(
    title="Modulux Homes API",
    description="Backend API cho dự án Modulux Homes - CMS đầy đủ tính năng với Soft Delete",
    version="2.0.0",
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    """Tự động tạo bảng trong DB khi server khởi động."""
    Base.metadata.create_all(bind=engine)


# Gắn toàn bộ Router API v1
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Modulux Homes API v2"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
