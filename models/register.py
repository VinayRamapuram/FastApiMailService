from sqlalchemy import Column, String, Integer
from database import Base


class RegisterDB(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)
