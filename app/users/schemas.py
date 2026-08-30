import pydantic


class UserLogin(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: str


class UserCreate(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: str
    first_name: str
    last_name: str
