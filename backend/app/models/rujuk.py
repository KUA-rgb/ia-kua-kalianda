from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Rujuk(Base):
    __tablename__ = "rujuk"
    
    id = Column(Integer, primary_key=True, index=True)
    nomor_akta = Column(String, unique=True, index=True)
    nama_suami = Column(String, index=True)
    nama_istri = Column(String, index=True)
    tanggal_rujuk = Column(Date)
    tanggal_pencatatan = Column(Date, nullable=True)
    tempat_rujuk = Column(String, nullable=True)
    status = Column(String, default="pending")
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
