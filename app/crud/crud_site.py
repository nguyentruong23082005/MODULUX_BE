from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.models.site import SiteSetting, Banner, CoreFeature, Video, Partner
from app.schemas.site import (
    SiteSettingCreate, SiteSettingUpdate,
    BannerCreate, BannerUpdate,
    CoreFeatureCreate, CoreFeatureUpdate,
    VideoCreate, VideoUpdate,
    PartnerCreate, PartnerUpdate,
)

_now = lambda: datetime.now(timezone.utc)


# ─── SiteSetting ────────────────────────────────────────────────
def get_settings(db: Session):
    return db.query(SiteSetting).filter(SiteSetting.delete_at == None).all()


def get_setting(db: Session, setting_id: int):
    return db.query(SiteSetting).filter(SiteSetting.id == setting_id, SiteSetting.delete_at == None).first()


def get_setting_by_key(db: Session, key_name: str):
    return db.query(SiteSetting).filter(SiteSetting.key_name == key_name, SiteSetting.delete_at == None).first()


def create_setting(db: Session, data: SiteSettingCreate):
    obj = SiteSetting(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_setting(db: Session, setting_id: int, data: SiteSettingUpdate):
    obj = get_setting(db, setting_id)
    if obj:
        for k, v in data.model_dump(exclude_none=True).items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj


def soft_delete_setting(db: Session, setting_id: int, deleted_by: int):
    obj = get_setting(db, setting_id)
    if obj:
        obj.delete_at = _now()
        obj.delete_by = deleted_by
        db.commit()
    return obj


# ─── Banner ─────────────────────────────────────────────────────
def get_banners(db: Session):
    return db.query(Banner).filter(Banner.delete_at == None).order_by(Banner.display_order).all()


def get_banner(db: Session, banner_id: int):
    return db.query(Banner).filter(Banner.id == banner_id, Banner.delete_at == None).first()


def create_banner(db: Session, data: BannerCreate):
    obj = Banner(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_banner(db: Session, banner_id: int, data: BannerUpdate):
    obj = get_banner(db, banner_id)
    if obj:
        for k, v in data.model_dump(exclude_none=True).items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj


def soft_delete_banner(db: Session, banner_id: int, deleted_by: int):
    obj = get_banner(db, banner_id)
    if obj:
        obj.delete_at = _now()
        obj.delete_by = deleted_by
        db.commit()
    return obj


# ─── CoreFeature ────────────────────────────────────────────────
def get_core_features(db: Session):
    return db.query(CoreFeature).filter(CoreFeature.delete_at == None).order_by(CoreFeature.display_order).all()


def get_core_feature(db: Session, feature_id: int):
    return db.query(CoreFeature).filter(CoreFeature.id == feature_id, CoreFeature.delete_at == None).first()


def create_core_feature(db: Session, data: CoreFeatureCreate):
    obj = CoreFeature(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_core_feature(db: Session, feature_id: int, data: CoreFeatureUpdate):
    obj = get_core_feature(db, feature_id)
    if obj:
        for k, v in data.model_dump(exclude_none=True).items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj


def soft_delete_core_feature(db: Session, feature_id: int, deleted_by: int):
    obj = get_core_feature(db, feature_id)
    if obj:
        obj.delete_at = _now()
        obj.delete_by = deleted_by
        db.commit()
    return obj


# ─── Video ──────────────────────────────────────────────────────
def get_videos(db: Session):
    return db.query(Video).filter(Video.delete_at == None).order_by(Video.display_order).all()


def get_video(db: Session, video_id: int):
    return db.query(Video).filter(Video.id == video_id, Video.delete_at == None).first()


def create_video(db: Session, data: VideoCreate):
    obj = Video(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_video(db: Session, video_id: int, data: VideoUpdate):
    obj = get_video(db, video_id)
    if obj:
        for k, v in data.model_dump(exclude_none=True).items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj


def soft_delete_video(db: Session, video_id: int, deleted_by: int):
    obj = get_video(db, video_id)
    if obj:
        obj.delete_at = _now()
        obj.delete_by = deleted_by
        db.commit()
    return obj


# ─── Partner ────────────────────────────────────────────────────
def get_partners(db: Session):
    return db.query(Partner).filter(Partner.delete_at == None).order_by(Partner.display_order).all()


def get_partner(db: Session, partner_id: int):
    return db.query(Partner).filter(Partner.id == partner_id, Partner.delete_at == None).first()


def create_partner(db: Session, data: PartnerCreate):
    obj = Partner(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_partner(db: Session, partner_id: int, data: PartnerUpdate):
    obj = get_partner(db, partner_id)
    if obj:
        for k, v in data.model_dump(exclude_none=True).items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj


def soft_delete_partner(db: Session, partner_id: int, deleted_by: int):
    obj = get_partner(db, partner_id)
    if obj:
        obj.delete_at = _now()
        obj.delete_by = deleted_by
        db.commit()
    return obj
