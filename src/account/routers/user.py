from fastapi import APIRouter
from src.account.schemas.user import users, UserListSchema, CreateUserSchema, UpdateUserSchema
import json
from pathlib import Path

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/health")
def health_handler():
    return {"work": "success"}

@router.get("/", response_model=list[UserListSchema])
def get_users_handler():
    return users

@router.post("/", response_model=UserListSchema)
def create_users_handler(payload: CreateUserSchema):
    user = {
        "id": len(users) + 1,
        "email": payload.email,
        "first_name": payload.first_name,
        "last_name": payload.last_name,
        "is_superuser": False,
        "is_active": False,
    }
    return user

@router.put("/{user_id}", response_model=UserListSchema)
def update_users_handler(
        user_id:int, #1,3,6
        payload: UpdateUserSchema
):
        user = [user for user in users if user.get("id") == user_id][0]

        user["first_name"] = payload.first_name
        user["last_name"] = payload.last_name
        return user