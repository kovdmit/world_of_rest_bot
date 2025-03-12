import os

from dotenv import load_dotenv


load_dotenv()

USERNAME = os.getenv('WOR_USERNAME')
PASSWORD = os.getenv('WOR_PASSWORD')
