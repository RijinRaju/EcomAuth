from pydantic import BaseModel


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: str
    phone: str