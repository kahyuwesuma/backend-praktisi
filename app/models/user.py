from sqlalchemy import Column, Integer, String
from app.db import Base
from app.security import verify_password

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    def verify_password(self, password: str):
        return verify_password(password, self.password)
