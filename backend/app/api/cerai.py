from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.cerai import Cerai
from app.schemas.cerai_schema import CeraiCreate, CeraiResponse, CeraiUpdate

router = APIRouter(prefix="/api/cerai", tags=["cerai"])

@router.get("/", response_model=list[CeraiResponse])
def get_all_cerai(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """Get all cerai data"""
    return db.query(Cerai).offset(skip).limit(limit).all()

@router.post("/", response_model=CeraiResponse, status_code=status.HTTP_201_CREATED)
def create_cerai(cerai: CeraiCreate, db: Session = Depends(get_db)):
    """Create new cerai record"""
    db_cerai = Cerai(**cerai.dict())
    db.add(db_cerai)
    db.commit()
    db.refresh(db_cerai)
    return db_cerai

@router.get("/{cerai_id}", response_model=CeraiResponse)
def get_cerai(cerai_id: int, db: Session = Depends(get_db)):
    """Get cerai by ID"""
    cerai = db.query(Cerai).filter(Cerai.id == cerai_id).first()
    if not cerai:
        raise HTTPException(status_code=404, detail="Cerai not found")
    return cerai

@router.put("/{cerai_id}", response_model=CeraiResponse)
def update_cerai(cerai_id: int, cerai_update: CeraiUpdate, db: Session = Depends(get_db)):
    """Update cerai record"""
    cerai = db.query(Cerai).filter(Cerai.id == cerai_id).first()
    if not cerai:
        raise HTTPException(status_code=404, detail="Cerai not found")
    
    update_data = cerai_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(cerai, field, value)
    
    db.commit()
    db.refresh(cerai)
    return cerai

@router.delete("/{cerai_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cerai(cerai_id: int, db: Session = Depends(get_db)):
    """Delete cerai record"""
    cerai = db.query(Cerai).filter(Cerai.id == cerai_id).first()
    if not cerai:
        raise HTTPException(status_code=404, detail="Cerai not found")
    
    db.delete(cerai)
    db.commit()
    return None

@router.get("/search/{query}")
def search_cerai(query: str, db: Session = Depends(get_db)):
    """Search cerai by name"""
    return db.query(Cerai).filter(
        (Cerai.nama_suami.ilike(f"%{query}%")) |
        (Cerai.nama_istri.ilike(f"%{query}%"))
    ).all()
