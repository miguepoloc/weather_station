"""JWT + hashing. No es uno de los 6 patrones de la clase, pero se conserva porque ya era un
buen ejemplo real (encapsula la creación/validación de tokens en una sola clase) y hace falta
para que /users funcione de punta a punta.
"""

from __future__ import annotations

import time

import bcrypt
import jwt

from app import constants


class Authorizer:
    def create_access_token(self, user_id: int) -> str:
        payload = {
            "sub": user_id,
            "expires_at": int(time.time()) + constants.EnvironmentVariables.TOKEN_API_EXPIRATION,
        }
        return jwt.encode(
            payload, key=constants.EnvironmentVariables.SECRET_API_KEY, algorithm=constants.EnvironmentVariables.ALGORITHM
        )

    def validate_and_decode_token(self, token: str) -> dict:
        return jwt.decode(
            token,
            key=constants.EnvironmentVariables.SECRET_API_KEY,
            algorithms=[constants.EnvironmentVariables.ALGORITHM],
        )


class Hasher:
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

    def get_password_hash(self, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
