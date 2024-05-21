from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']


SQL_DATABASE_URL =  f'postgresql://{db_user}:{db_password}@localhost:5432/ecom_auth'
engine = create_engine(SQL_DATABASE_URL)
sessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

# to end the session
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
