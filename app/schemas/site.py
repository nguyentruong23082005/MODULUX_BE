from pydantic import BaseModel, ConfigDict
from typing import Optional


# ─── SiteSetting ───────────────────────────────────────────────
class SiteSettingCreate(BaseModel):
    key_name: str
    value: str
    description: Optional[str] = None


class SiteSettingUpdate(BaseModel):
    value: Optional[str] = None
    description: Optional[str] = None


class SiteSettingOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    key_name: str
    value: str
    description: Optional[str] = None


# ─── Banner ──────────────────────────────────────────────────────
class BannerCreate(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    media_url: str
    button_text: Optional[str] = None
    button_link: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = True


class BannerUpdate(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    media_url: Optional[str] = None
    button_text: Optional[str] = None
    button_link: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class BannerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: Optional[str] = None
    subtitle: Optional[str] = None
    media_url: str
    button_text: Optional[str] = None
    button_link: Optional[str] = None
    display_order: Optional[int] = None
    is_active: bool


# ─── CoreFeature ────────────────────────────────────────────────
class CoreFeatureCreate(BaseModel):
    title: str
    description: Optional[str] = None
    icon_url: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = True


class CoreFeatureUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    icon_url: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class CoreFeatureOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str] = None
    icon_url: Optional[str] = None
    display_order: Optional[int] = None
    is_active: bool


# ─── Video ──────────────────────────────────────────────────────
class VideoCreate(BaseModel):
    title: Optional[str] = None
    video_url: str
    thumbnail_url: Optional[str] = None
    display_order: Optional[int] = None


class VideoUpdate(BaseModel):
    title: Optional[str] = None
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    display_order: Optional[int] = None


class VideoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: Optional[str] = None
    video_url: str
    thumbnail_url: Optional[str] = None
    display_order: Optional[int] = None


# ─── Partner ────────────────────────────────────────────────────
class PartnerCreate(BaseModel):
    name: str
    logo_url: str
    display_order: Optional[int] = None


class PartnerUpdate(BaseModel):
    name: Optional[str] = None
    logo_url: Optional[str] = None
    display_order: Optional[int] = None


class PartnerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    logo_url: str
    display_order: Optional[int] = None
