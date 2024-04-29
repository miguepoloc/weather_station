from pydantic import BaseModel, EmailStr, field_validator

password_regex = r"((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})"


class UserSignin(BaseModel):
    """
    Class for serializing the user signin.

    keys:
    - email: The user email.
    - password: The user password.
    """

    email: EmailStr
    password: str

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
