from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    document: Optional[str] = None
    code_phone: Optional[str] = None
    phone_number: Optional[str] = None
    is_admin: bool = False
    is_superuser: bool = False
    profile_image: Optional[str] = None
    city: Optional[str] = None

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        """Validate the password format."""
        special_characters = "!@#$%^&*()-+"
        if len(value) < 8:
            raise ValueError("Invalid password. Expected length: 8")
        if not any(char.isdigit() for char in value):
            raise ValueError("Invalid password. Expected digits")
        if not any(char.isupper() for char in value):
            raise ValueError("Invalid password. Expected uppercase letter")
        if not any(char.islower() for char in value):
            raise ValueError("Invalid password. Expected lowercase letter")
        if not any(char in special_characters for char in value):
            raise ValueError("Invalid password. Expected special character")
        return value

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        """Validate the email format."""
        if not value.endswith("@gmail.com"):
            raise ValueError("Invalid email. Expected gmail domain")
        return value
