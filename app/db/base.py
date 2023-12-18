from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

class CustomBase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)

    @classmethod
    def __declare_last__(cls):
        cls.__tablename__ = cls.__name__.lower()
