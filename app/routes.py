from fastapi import APIRouter
from app.service import import_users

router = APIRouter()

@router.get("/")
def home():
    return {"message": "CSV Importer API Running"}

@router.post("/import")
def import_data():
    return import_users()
