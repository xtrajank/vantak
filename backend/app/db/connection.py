'''handles connection to db'''
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_connection():
    '''Connect to db with .env credentials'''
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
