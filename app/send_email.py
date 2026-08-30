"""Envío de correo vía Resend. Si no hay API key configurada (caso normal en clase), no falla:
imprime lo que habría enviado. Así el Observer de más abajo se puede demostrar sin que cada
estudiante necesite una cuenta de Resend real.
"""

from app import constants


def send(to_email: list[str], subject: str, html: str) -> dict:
    if not constants.EnvironmentVariables.EMAIL_RESEND_API_KEY:
        print(f"[email simulado] to={to_email} subject={subject!r}")
        return {"simulated": True}

    import resend

    resend.api_key = constants.EnvironmentVariables.EMAIL_RESEND_API_KEY
    return resend.Emails.send(
        {
            "from": constants.EnvironmentVariables.EMAIL_FROM,
            "to": to_email,
            "subject": subject,
            "html": html,
        }
    )
