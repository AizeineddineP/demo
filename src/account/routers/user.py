from fastapi import APIRouter
from src.account.schemas.user import users, UserListSchema
import json
from pathlib import Path

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/health")
def health_handler():
    return {"work": "success"}

@router.get("/", response_model=UserListSchema)
def get_users_handler():
    file_path = Path("users.json")
    return json.loads(file_path.read_text())