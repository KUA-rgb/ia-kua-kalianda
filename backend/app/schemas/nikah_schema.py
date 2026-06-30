from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class NikahBase(BaseModel):
    nomor_akta: str
    nama_pengantin_pria: str
    nama_pengantin_wanita: str
    tanggal_nikah: date
    tanggal_pencatatan: Optional[date] = None
    tempat_nikah: Optional[str] = None

class NikahCreate(NikahBase):
    pass

class NikahUpdate(BaseModel):
    nomor_akta: Optional[str] = None
    nama_pengantin_pria: Optional[str] = None
    nama_pengantin_wanita: Optional[str] = None
    tanggal_nikah: Optional[date] = None
    tanggal_pencatatan: Optional[date] = None
    tempat_nikah: Optional[str] = None
    status: Optional[str] = None

class NikahResponse(NikahBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
