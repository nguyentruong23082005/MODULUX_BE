from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.api.deps import get_current_user
from app.schemas.site import VideoCreate, VideoUpdate, VideoOut
from app.crud.crud_site import get_videos, get_video, create_video, update_video, soft_delete_video
from app.models.user import User

router = APIRouter(prefix="/videos", tags=["Videos"])


@router.get("/", response_model=List[VideoOut])
def list_videos(db: Session = Depends(get_db)):
    return get_videos(db)


@router.get("/{video_id}", response_model=VideoOut)
def get_one(video_id: int, db: Session = Depends(get_db)):
    obj = get_video(db, video_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Video not found")
    return obj


@router.post("/", response_model=VideoOut, status_code=201)
def create(data: VideoCreate, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    return create_video(db, data)


@router.put("/{video_id}", response_model=VideoOut)
def update(video_id: int, data: VideoUpdate, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    obj = update_video(db, video_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Video not found")
    return obj


@router.delete("/{video_id}", status_code=204)
def delete(video_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    obj = get_video(db, video_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Video not found")
    soft_delete_video(db, video_id, deleted_by=current_user.id)
