from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()

user = os.getenv("DB_USER")
password = urllib.parse.quote_plus(os.getenv("DB_PASS"))
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

sqlalchemy_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(sqlalchemy_url)
Session = sessionmaker(bind=engine)
session = Session()
