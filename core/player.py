from models import register
from hashing import Hash
from fastapi import HTTPException, status


def create_user(request, db):
    new_user = register.RegisterDB(email=request.email, password=Hash.bcrypt(request.password), name=request.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(email, db):
    us = db.query(register.RegisterDB).filter(register.RegisterDB.email == email).first()
    if not register:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"email {email} does not exists")

    return us
