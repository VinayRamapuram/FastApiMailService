from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pwd_context.hash(password)

    @staticmethod
    def verify(db_pwd, ui_pwd):
        return pwd_context.verify(ui_pwd, db_pwd)

