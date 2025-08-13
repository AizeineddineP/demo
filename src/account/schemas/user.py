from pydantic import BaseModel

users = [
    {
      "id":1,
      "email" : "user_1.cdd",
      "first_name": "anton",
      "last_name": "antonov",
      "is_superuser": False,
    },
    {
        "id":2,
        "email": "user_2.cdd",
        "first_name": "sasha",
        "last_name": "anonov",
    },
    {
        "id":3,
        "email": "user_3.cdd",
        "first_name": "ali",
        "last_name": "fadi",
        "is_superuser": False,
        "is_active": True,
    },
    {
        "id":4,
        "email": "user_4.cdd",
        "first_name": "rawa",
        "last_name": "antonov",
        "is_superuser": False,
    },

]

class BaseUserSchema(BaseModel):
    email: str
    first_name: str
    last_name: str

class UserListSchema(BaseUserSchema):
    id: int
    is_superuser: bool | None = None
    is_active: bool | None = None

class CreateUserSchema(BaseUserSchema):
        pass


class UpdateUserSchema(BaseUserSchema):
    first_name: str
    last_name: str