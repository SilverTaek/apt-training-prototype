# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))  # ← 숫자로 변환
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
MAIL_FROM  = os.getenv("MAIL_FROM", "")

# 회사/프록시 CA 체인 파일 경로 (없으면 빈 문자열)
COMPANY_CA_FILE = os.getenv("COMPANY_CA_FILE", "").strip()
