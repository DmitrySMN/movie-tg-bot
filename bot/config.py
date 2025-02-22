import os
from dotenv import load_dotenv
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker


load_dotenv(dotenv_path='../.env')

engine = create_engine(os.getenv('DATABASE_URI'))

Session = sessionmaker(bind=engine)
