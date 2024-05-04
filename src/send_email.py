import os

<<<<<<< HEAD
resend.api_key = 're_NAug4g3v_BnmjtnvDdLhBEcq7emL15wUj'
=======
import resend

resend.api_key = os.getenv("EMAIL_RESEND_API_KEY")
>>>>>>> 90c055075f45b469f8440d0a49484db60d986c25


def send_email(to_email: list, subject: str, html: str) -> dict:
    send: dict = resend.Emails.send(
        {
<<<<<<< HEAD
            "from": os.environ['EMAIL_FROM'],
=======
            "from": os.getenv("EMAIL_FROM"),
>>>>>>> 90c055075f45b469f8440d0a49484db60d986c25
            "to": to_email,
            "subject": subject,
            "html": html,
        }
    )
    return send
