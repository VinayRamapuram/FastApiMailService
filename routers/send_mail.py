from fastapi import BackgroundTasks, APIRouter
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List
from data import body_data, recipients


router = APIRouter(tags=['send_mail'])


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


@router.post("/email")
async def simple_send() -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=recipients,  # List of recipients, as many as you can pass
        template_body=body_data,
        )
    fm = FastMail(conf)
    await fm.send_message(message, template_name="email.html")
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@router.post("/emailbackground")
async def send_in_background(background_tasks: BackgroundTasks) -> JSONResponse:
    message = MessageSchema(
        subject="Background Fastapi mail module ",
        recipients=recipients,
        template_body=body_data,
        )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name="email.html")

    return JSONResponse(status_code=200, content={"message": "email has been sent"})