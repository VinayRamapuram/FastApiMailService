import uvicorn
from fastapi import FastAPI
from models import register as user_models
from database import engine
from routers import user, send_mail, authentication, oauth2


user_models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(authentication.router)
app.include_router(oauth2.router)
app.include_router(user.router)
app.include_router(send_mail.router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)