import os


resend.api_key = os.getenv("EMAIL_RESEND_API_KEY")


def send_email(to_email: list, subject: str, html: str) -> dict:
    send: dict = resend.Emails.send(
        {
            "from": os.getenv("EMAIL_FROM"),
            "to": to_email,
            "subject": subject,
            "html": html,
        }
    )
    return send
