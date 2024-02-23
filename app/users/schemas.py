from pydantic import BaseModel, EmailStr


class SUserAUth(BaseModel):
    email: EmailStr
    password: str
