from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.api.deps import get_db, get_current_admin
from app.models.sweet import Sweet
from app.schemas.sweet import SweetCreate, SweetUpdate, SweetResponse

router = APIRouter(prefix="/api/sweets", tags=["sweets"])


@router.get("/", response_model=List[SweetResponse])
def get_sweets(db: Session = Depends(get_db)):
    return db.query(Sweet).all()


@router.get("/search", response_model=List[SweetResponse])
def search_sweets(
    name: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    db: Session = Depends(get_db),
):
    query = db.query(Sweet)

    if name:
        query = query.filter(Sweet.name.ilike(f"%{name}%"))
    if category:
        query = query.filter(Sweet.category.ilike(f"%{category}%"))
    if min_price is not None:
        query = query.filter(Sweet.price >= min_price)
    if max_price is not None:
        query = query.filter(Sweet.price <= max_price)

    return query.all()


@router.post("/", response_model=SweetResponse)
def create_sweet(
    data: SweetCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin),
):
    sweet = Sweet(**data.model_dump())
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet


@router.put("/{sweet_id}", response_model=SweetResponse)
def update_sweet(
    sweet_id: int,
    data: SweetUpdate,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin),
):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(sweet, key, value)

    db.commit()
    db.refresh(sweet)
    return sweet


@router.delete("/{sweet_id}")
def delete_sweet(
    sweet_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin),
):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    db.delete(sweet)
    db.commit()
    return {"message": "Sweet deleted successfully"}
