"""Variables de entorno de la aplicación, con valores por defecto pensados para clase.

En un proyecto real estos defaults no existirían (un SECRET_API_KEY faltante debería tumbar el
arranque). Aquí se usan para que la API funcione "de una" sin pedirle a cada estudiante que arme
un .env completo antes de poder ver los patrones en acción.
"""

import os


class EnvironmentVariables:
    DB_BACKEND: str = os.getenv("DB_BACKEND", "sqlite")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./estacion_clima.db")

    SECRET_API_KEY: str = os.getenv("SECRET_API_KEY", "dev-secret-key-cambiame")
    TOKEN_API_EXPIRATION: int = int(os.getenv("TOKEN_API_EXPIRATION", "3600"))
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")

    EMAIL_RESEND_API_KEY: str | None = os.getenv("EMAIL_RESEND_API_KEY")
    EMAIL_FROM: str = os.getenv("EMAIL_FROM", "estacion@example.com")
    ALERT_EMAIL_TO: str = os.getenv("ALERT_EMAIL_TO", "docente@example.com")
