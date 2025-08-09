from pydantic import BaseModel

users = [
    {
      "email" : "email.cdd",
      "first_name": "anton",
      "last_name": "antonov",
      "is_superuser": False,
    },
    {
        "email": "gergel.cdd",
        "first_name": "sasha",
        "last_name": "anonov",
    },
    {
        "email": "edgfl.cdd",
        "first_name": "ali",
        "last_name": "fadi",
        "is_superuser": False,
        "is_active": True,
    },
    {
        "email": "fdgghl.cdd",
        "first_name": "rawa",
        "last_name": "antonov",
        "is_superuser": False,
    },

]



class UserListSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    is_superuser: bool | None = None
    is_active: bool | None = None

