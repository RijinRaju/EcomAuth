from sqlalchemy import Column, Integer, String, Boolean
from app.config.db import Base, engine

class User(Base):
    __tablename__ = 'users'

    id  = Column(Integer, primary_key= True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String)
    is_active = Column(Boolean, default=True)

Base.metadata.create_all(bind = engine)