from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class RujukBase(BaseModel):
    nomor_akta: str
    nama_suami: str
    nama_istri: str
    tanggal_rujuk: date
    tanggal_pencatatan: Optional[date] = None
    tempat_rujuk: Optional[str] = None

class RujukCreate(RujukBase):
    pass

class RujukUpdate(BaseModel):
    nomor_akta: Optional[str] = None
    nama_suami: Optional[str] = None
    nama_istri: Optional[str] = None
    tanggal_rujuk: Optional[date] = None
    tanggal_pencatatan: Optional[date] = None
    tempat_rujuk: Optional[str] = None
    status: Optional[str] = None

class RujukResponse(RujukBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
