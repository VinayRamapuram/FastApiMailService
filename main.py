from fastapi import (
    FastAPI,
    BackgroundTasks,
    UploadFile, File,
    Form,
    Query,
    Body,
    Depends
)
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List, Dict, Any
from fastapi_mail.email_utils import DefaultChecker
import uvicorn
from data import body_data, recipients


class EmailSchema(BaseModel):
    email: List[EmailStr]
    # body: Dict[str, Any]


conf = ConnectionConfig(
    MAIL_USERNAME="vinaymouse2@gmail.com",
    MAIL_PASSWORD="Vinay$1994",
    MAIL_FROM="vinaymouse2@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Vinay R",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER='./templates'

)

app = FastAPI()


@app.post("/email")
async def simple_send() -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=recipients,  # List of recipients, as many as you can pass
        template_body=body_data,
        )
    fm = FastMail(conf)
    await fm.send_message(message, template_name="email.html")
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@app.post("/emailbackground")
async def send_in_background(background_tasks: BackgroundTasks) -> JSONResponse:
    message = MessageSchema(
        subject="Background Fastapi mail module ",
        recipients=recipients,
        template_body=body_data,
        )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name="email.html")

    return JSONResponse(status_code=200, content={"message": "email has been sent"})


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)