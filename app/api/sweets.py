from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.sweet import Sweet
from app.schemas.sweet import SweetCreate, SweetOut
from app.api.deps import get_db, get_current_user, admin_only

router = APIRouter(prefix="/api/sweets", tags=["sweets"])


@router.get("", response_model=list[SweetOut])
def list_sweets(db: Session = Depends(get_db)):
    return db.query(Sweet).all()


@router.post("", response_model=SweetOut)
def add_sweet(
    data: SweetCreate,
    db: Session = Depends(get_db),
    _=Depends(admin_only),
):
    sweet = Sweet(**data.model_dump())
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet


@router.post("/{sweet_id}/purchase")
def purchase_sweet(
    sweet_id: int,
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    sweet = db.get(Sweet, sweet_id)
    if not sweet or sweet.quantity <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")

    sweet.quantity -= 1
    db.commit()
    return {"status": "purchased"}


@router.post("/{sweet_id}/restock")
def restock_sweet(
    sweet_id: int,
    quantity: int,
    db: Session = Depends(get_db),
    _=Depends(admin_only),
):
    sweet = db.get(Sweet, sweet_id)
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    sweet.quantity += quantity
    db.commit()
    return {"status": "restocked"}
