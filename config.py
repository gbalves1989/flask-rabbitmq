from dotenv import load_dotenv
import os


load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

SECRET_KEY = os.environ.get('SECRET_KEY')

MQ_EXCHANGE = os.environ.get('MQ_EXCHANGE')
MQ_URL = os.environ.get('MQ_URL')
