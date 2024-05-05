"""This module contains the constants used in the application."""

import os


class EnvironmentVariables:
    """
    This class represents the environment variables used in the application.

    Note:
        The values for these attributes are retrieved from environment variables using the `os.getenv` function.
    """
"""
    SECRET_API_KEY: str = os.getenv("SECRET_API_KEY")  # type: ignore
    TOKEN_API_EXPIRATION: int = int(os.getenv("TOKEN_API_EXPIRATION"))  # type: ignore
    ENVIRONMENT: str = os.getenv("ENVIRONMENT")  # type: ignore
    DEBUG: bool = os.getenv("DEBUG")  # type: ignore
    AWS_S3_BUCKET_NAME: str = os.getenv("ENV_BUCKET_NAME")  # type: ignore
    ALGORITHM: str = os.getenv("ALGORITHM")  # type: ignore
"""