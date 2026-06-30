from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.rujuk import Rujuk
from app.schemas.rujuk_schema import RujukCreate, RujukResponse, RujukUpdate

router = APIRouter(prefix="/api/rujuk", tags=["rujuk"])

@router.get("/", response_model=list[RujukResponse])
def get_all_rujuk(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """Get all rujuk data"""
    return db.query(Rujuk).offset(skip).limit(limit).all()

@router.post("/", response_model=RujukResponse, status_code=status.HTTP_201_CREATED)
def create_rujuk(rujuk: RujukCreate, db: Session = Depends(get_db)):
    """Create new rujuk record"""
    db_rujuk = Rujuk(**rujuk.dict())
    db.add(db_rujuk)
    db.commit()
    db.refresh(db_rujuk)
    return db_rujuk

@router.get("/{rujuk_id}", response_model=RujukResponse)
def get_rujuk(rujuk_id: int, db: Session = Depends(get_db)):
    """Get rujuk by ID"""
    rujuk = db.query(Rujuk).filter(Rujuk.id == rujuk_id).first()
    if not rujuk:
        raise HTTPException(status_code=404, detail="Rujuk not found")
    return rujuk

@router.put("/{rujuk_id}", response_model=RujukResponse)
def update_rujuk(rujuk_id: int, rujuk_update: RujukUpdate, db: Session = Depends(get_db)):
    """Update rujuk record"""
    rujuk = db.query(Rujuk).filter(Rujuk.id == rujuk_id).first()
    if not rujuk:
        raise HTTPException(status_code=404, detail="Rujuk not found")
    
    update_data = rujuk_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(rujuk, field, value)
    
    db.commit()
    db.refresh(rujuk)
    return rujuk

@router.delete("/{rujuk_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rujuk(rujuk_id: int, db: Session = Depends(get_db)):
    """Delete rujuk record"""
    rujuk = db.query(Rujuk).filter(Rujuk.id == rujuk_id).first()
    if not rujuk:
        raise HTTPException(status_code=404, detail="Rujuk not found")
    
    db.delete(rujuk)
    db.commit()
    return None

@router.get("/search/{query}")
def search_rujuk(query: str, db: Session = Depends(get_db)):
    """Search rujuk by name"""
    return db.query(Rujuk).filter(
        (Rujuk.nama_suami.ilike(f"%{query}%")) |
        (Rujuk.nama_istri.ilike(f"%{query}%"))
    ).all()
