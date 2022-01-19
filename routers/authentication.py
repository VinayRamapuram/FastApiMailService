from fastapi import APIRouter, Depends, HTTPException, status
from routers.JWT_Token import create_access_token
import schemas
from schemas import Login
from sqlalchemy.orm import Session
from database import get_db
from models.register import RegisterDB
from hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    valid_user = db.query(RegisterDB).filter(RegisterDB.email == request.username).first()
    if not valid_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    if not Hash.verify(valid_user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is not correct")

    access_token = create_access_token(data={'email': valid_user.email, 'name': valid_user.name})

    return {"access_token": access_token, "token_type": 'bearer'}
