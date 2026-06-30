from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.database import get_db
from app.models.nikah import Nikah
from app.models.cerai import Cerai
from app.models.rujuk import Rujuk

router = APIRouter(prefix="/api", tags=["stats"])

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    """Get dashboard statistics"""
    today = datetime.now().date()
    month_start = datetime(today.year, today.month, 1).date()
    
    total_nikah = db.query(func.count(Nikah.id)).scalar()
    total_cerai = db.query(func.count(Cerai.id)).scalar()
    total_rujuk = db.query(func.count(Rujuk.id)).scalar()
    
    bulan_ini = db.query(func.count(Nikah.id)).filter(
        Nikah.created_at >= month_start
    ).scalar() + db.query(func.count(Cerai.id)).filter(
        Cerai.created_at >= month_start
    ).scalar() + db.query(func.count(Rujuk.id)).filter(
        Rujuk.created_at >= month_start
    ).scalar()
    
    nikah_terbaru = db.query(Nikah).order_by(Nikah.created_at.desc()).limit(5).all()
    cerai_terbaru = db.query(Cerai).order_by(Cerai.created_at.desc()).limit(5).all()
    rujuk_terbaru = db.query(Rujuk).order_by(Rujuk.created_at.desc()).limit(5).all()
    
    return {
        "total_nikah": total_nikah or 0,
        "total_cerai": total_cerai or 0,
        "total_rujuk": total_rujuk or 0,
        "bulan_ini": bulan_ini or 0,
        "nikah_terbaru": nikah_terbaru,
        "cerai_terbaru": cerai_terbaru,
        "rujuk_terbaru": rujuk_terbaru
    }
