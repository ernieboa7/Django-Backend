from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_products(db: Session = Depends(get_db)):
    return db.execute("SELECT * FROM products_product").fetchall()
