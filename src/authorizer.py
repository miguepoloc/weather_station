"""
This module contains the authorizer function to validate the JWT token.
"""

import time

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

from src.constants import EnvironmentVariables

security = HTTPBearer()


class Authorizer:
    """
    The Authorizer class provides methods for creating, validating, and decoding JWT tokens.
    """

    def create_access_token(self, user_id: int) -> str:
        """
        Creates an access token for a user.

        Parameters:
            user_id (int): The ID of the user.

        Returns:
            str: The encoded JWT access token.
        """
        data: dict[str, int] = {"sub": user_id}
        expires_at: int = int(time.time()) + EnvironmentVariables.TOKEN_API_EXPIRATION
        data["expires_at"] = expires_at
        encode_data: str = jwt.encode(
            payload=data, key=EnvironmentVariables.SECRET_API_KEY, algorithm=EnvironmentVariables.ALGORITHM
        )
        return encode_data

    def validate_and_decode_token(self, token: str) -> dict[str, str]:
        """
        Validates and decodes a JWT token.

        Parameters:
            token (str): The JWT token to validate and decode.

        Returns:
            dict[str, str]: The decoded JWT token payload.

        Raises:
            HTTPException:
                - 401 Unauthorized if the token is expired or invalid.
                - 401 Unauthorized if there is an unexpected error.
                - 401 Unauthorized if the token is not provided.
        """
        try:
            return jwt.decode(token, key=EnvironmentVariables.SECRET_API_KEY, algorithms=EnvironmentVariables.ALGORITHM)
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except Exception:
            raise HTTPException(status_code=401, detail="You are not permission")

    def get_data_authorizer(self, request: Request) -> dict[str, str]:
        """
        Extracts and validates the JWT token from the request headers.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            dict[str, str]: The decoded JWT token payload.

        Raises:
            HTTPException:
                - 401 Unauthorized if the token is expired or invalid.
                - 401 Unauthorized if there is an unexpected error.
                - 401 Unauthorized if the token is not provided.
        """
        token_data: str = request.headers.get("Authorization", "")
        try:
            token: str = token_data.split(" ")[1]
            token_decode: dict[str, str] = self.validate_and_decode_token(token=token)
            return token_decode
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except Exception:
            raise HTTPException(status_code=401, detail="You are not permission")


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security), authorizer: Authorizer = Depends(Authorizer)
) -> dict[str, str]:
    try:
        payload: dict[str, str] = authorizer.validate_and_decode_token(credentials.credentials)
    except HTTPException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload


class Hasher:
    """
    The Hasher class provides methods for password hashing and verification.
    """

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verifies if a plain password matches a hashed password.

        Args:
            plain_password (str): The plain password to be verified.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the plain password matches the hashed password, False otherwise.
        """
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        """
        Generates a hash for a given password.

        Args:
            password (str): The password to be hashed.

        Returns:
            str: The hashed password.
        """
        return self.pwd_context.hash(password)
