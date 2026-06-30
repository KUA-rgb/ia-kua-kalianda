from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class CeraiBase(BaseModel):
    nomor_akta: str
    nama_suami: str
    nama_istri: str
    tanggal_cerai: date
    tanggal_pencatatan: Optional[date] = None
    pengadilan: Optional[str] = None

class CeraiCreate(CeraiBase):
    pass

class CeraiUpdate(BaseModel):
    nomor_akta: Optional[str] = None
    nama_suami: Optional[str] = None
    nama_istri: Optional[str] = None
    tanggal_cerai: Optional[date] = None
    tanggal_pencatatan: Optional[date] = None
    pengadilan: Optional[str] = None
    status: Optional[str] = None

class CeraiResponse(CeraiBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
