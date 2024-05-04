"""This module contains the constants used in the application."""

import os


class EnvironmentVariables:
    """
    This class represents the environment variables used in the application.

    Note:
        The values for these attributes are retrieved from environment variables using the `os.getenv` function.
    """

    SECRET_API_KEY: str = "secret_key"  # type: ignore
    TOKEN_API_EXPIRATION: int = 3600  # type: ignore
    ENVIRONMENT: str = os.getenv("ENVIRONMENT")  # type: ignore
    DEBUG: bool = os.getenv("DEBUG")  # type: ignore
    AWS_S3_BUCKET_NAME: str = os.getenv("ENV_BUCKET_NAME")  # type: ignore
    ALGORITHM: str = "HS256" # type: ignore
