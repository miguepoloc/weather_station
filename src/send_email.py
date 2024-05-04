import resend
import os

resend.api_key = "re_LQKnbkUN_6c3PRXGLQjLVetnm7gvTPKdJ"


def send_email(to_email: list, subject: str, html: str) -> dict:
    send: dict = resend.Emails.send(
        {
            "from": os.environ["EMAIL_FROM"],
            "to": to_email,
            "subject": subject,
            "html": html,
        }
    )
    return send
