from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.services.mailer import send_mail

app = FastAPI(title="APT Training Prototype")

class MailRequest(BaseModel):
    to: List[EmailStr]
    subject: str
    html: str
    sender: Optional[EmailStr] = None  # 옵션: 보내는 주소 오버라이드
    sender_name: Optional[str] = None

@app.post("/mail/send")
def mail_send(req: MailRequest):
    send_mail(
        to=req.to, subject=req.subject, html=req.html,
        sender=req.sender, display_name=req.sender_name  # ⬅️ 변경
    )
    return {"status": "ok", "count": len(req.to)}
