import smtplib, ssl, certifi
from email.mime.text import MIMEText
from email.utils import formataddr
from typing import List
from app.core.config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, MAIL_FROM

def send_mail(to: List[str], subject: str, html: str, sender: str | None = None):
    if not SMTP_HOST:
        raise RuntimeError("SMTP_HOST is not set")

    msg = MIMEText(html, "html", "utf-8")
    msg["Subject"] = subject
    msg["From"] = formataddr(("APT Training", sender or MAIL_FROM))
    msg["To"] = ", ".join(to)

    # 기본: 587 + STARTTLS
    context = ssl.create_default_context(cafile=certifi.where())
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.ehlo()
        if SMTP_PORT == 587:
            s.starttls(context=context)
            s.ehlo()
        if SMTP_USER and SMTP_PASS:
            s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(sender or MAIL_FROM, to, msg.as_string())