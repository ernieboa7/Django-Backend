from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def search_products():
    return {"results": []}