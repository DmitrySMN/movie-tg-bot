from sqlalchemy import create_engine, Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    favorites = Column(ARRAY(Integer))
