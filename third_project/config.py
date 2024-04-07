import os
from dotenv import load_dotenv


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///tea_time.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True