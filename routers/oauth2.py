from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from routers.JWT_Token import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


router = APIRouter(tags=['oauth'])


@router.get('/user_data')
def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)


