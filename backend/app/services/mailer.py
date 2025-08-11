# app/services/mailer.py
import smtplib, ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from typing import List, Optional
import os
import certifi

from app.core.config import (
    SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, MAIL_FROM, COMPANY_CA_FILE
)

def build_ssl_context() -> ssl.SSLContext:
    """
    - 시스템 기본 신뢰 저장소
    - certifi 번들
    - 회사/프록시 CA 파일 (있으면)
    순으로 '추가' 로드하여 검증 실패를 최소화합니다.
    """
    ctx = ssl.create_default_context()
    # certifi 번들 추가 (예외 무시 가능)
    try:
        ctx.load_verify_locations(cafile=certifi.where())
    except Exception:
        pass
    # 회사 CA 체인 추가
    if COMPANY_CA_FILE and os.path.exists(COMPANY_CA_FILE):
        ctx.load_verify_locations(cafile=COMPANY_CA_FILE)
    return ctx

def send_mail(
    to: List[str],
    subject: str,
    html: str,
    sender: Optional[str] = None,
    display_name: Optional[str] = None,
):
    if not SMTP_HOST or not SMTP_PORT:
        raise RuntimeError("SMTP_HOST/SMTP_PORT 미설정")

    msg = MIMEText(html, "html", "utf-8")
    msg["Subject"] = subject
    msg["From"] = formataddr((display_name or "APT Training", sender or MAIL_FROM))
    msg["To"] = ", ".join(to)

    ctx = build_ssl_context()

    if SMTP_PORT == 465:
        # SSL 전용
        with smtplib.SMTP_SSL(SMTP_HOST, 465, context=ctx, timeout=15) as s:
            s.set_debuglevel(1)  # 문제 해결되면 0으로 바꿔도 됨
            if SMTP_USER and SMTP_PASS:
                s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(sender or MAIL_FROM, to, msg.as_string())

    elif SMTP_PORT == 587:
        # STARTTLS
        with smtplib.SMTP(SMTP_HOST, 587, timeout=15) as s:
            s.set_debuglevel(1)
            s.ehlo()
            s.starttls(context=ctx)
            s.ehlo()
            if SMTP_USER and SMTP_PASS:
                s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(sender or MAIL_FROM, to, msg.as_string())

    elif SMTP_PORT == 25:
        # 사내 릴레이(무인증일 수 있음)
        with smtplib.SMTP(SMTP_HOST, 25, timeout=15) as s:
            s.set_debuglevel(1)
            s.ehlo()
            # 필요시 정책에 따라 s.starttls(context=ctx)
            if SMTP_USER and SMTP_PASS:
                s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(sender or MAIL_FROM, to, msg.as_string())

    else:
        raise RuntimeError(f"지원하지 않는 SMTP 포트: {SMTP_PORT}")
