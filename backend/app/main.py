from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.services.mailer import send_mail

app = FastAPI(title="APT Training Prototype")

class MailRequest(BaseModel):
    to: List[str]
    subject: str
    html: str
    sender: Optional[str] = None  # 옵션: 보내는 주소 오버라이드

@app.post("/mail/send")
def mail_send(req: MailRequest):
    try:
        send_mail(to=req.to, subject=req.subject, html=req.html, sender=req.sender)
        return {"status": "ok", "count": len(req.to)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
