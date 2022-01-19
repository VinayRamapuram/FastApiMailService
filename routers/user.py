from fastapi import APIRouter, Depends,  HTTPException, status
import schemas
from database import get_db
from sqlalchemy.orm import Session
from core import player
from models import register
from routers import oauth2

router = APIRouter(tags=['player'])


@router.post('/create', response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return player.create_user(request, db)


@router.get('/{email}', response_model=schemas.ShowUser)
def get_user(email: str, db: Session = Depends(get_db),
             current_user: schemas.User = Depends(oauth2.get_current_user)):
    return player.get_user(email, db)
