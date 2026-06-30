from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.nikah import Nikah
from app.schemas.nikah_schema import NikahCreate, NikahResponse, NikahUpdate

router = APIRouter(prefix="/api/nikah", tags=["nikah"])

@router.get("/", response_model=list[NikahResponse])
def get_all_nikah(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """Get all nikah data"""
    return db.query(Nikah).offset(skip).limit(limit).all()

@router.post("/", response_model=NikahResponse, status_code=status.HTTP_201_CREATED)
def create_nikah(nikah: NikahCreate, db: Session = Depends(get_db)):
    """Create new nikah record"""
    db_nikah = Nikah(**nikah.dict())
    db.add(db_nikah)
    db.commit()
    db.refresh(db_nikah)
    return db_nikah

@router.get("/{nikah_id}", response_model=NikahResponse)
def get_nikah(nikah_id: int, db: Session = Depends(get_db)):
    """Get nikah by ID"""
    nikah = db.query(Nikah).filter(Nikah.id == nikah_id).first()
    if not nikah:
        raise HTTPException(status_code=404, detail="Nikah not found")
    return nikah

@router.put("/{nikah_id}", response_model=NikahResponse)
def update_nikah(nikah_id: int, nikah_update: NikahUpdate, db: Session = Depends(get_db)):
    """Update nikah record"""
    nikah = db.query(Nikah).filter(Nikah.id == nikah_id).first()
    if not nikah:
        raise HTTPException(status_code=404, detail="Nikah not found")
    
    update_data = nikah_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(nikah, field, value)
    
    db.commit()
    db.refresh(nikah)
    return nikah

@router.delete("/{nikah_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_nikah(nikah_id: int, db: Session = Depends(get_db)):
    """Delete nikah record"""
    nikah = db.query(Nikah).filter(Nikah.id == nikah_id).first()
    if not nikah:
        raise HTTPException(status_code=404, detail="Nikah not found")
    
    db.delete(nikah)
    db.commit()
    return None

@router.get("/search/{query}")
def search_nikah(query: str, db: Session = Depends(get_db)):
    """Search nikah by name"""
    return db.query(Nikah).filter(
        (Nikah.nama_pengantin_pria.ilike(f"%{query}%")) |
        (Nikah.nama_pengantin_wanita.ilike(f"%{query}%"))
    ).all()
