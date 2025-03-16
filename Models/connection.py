from dotenv import load_dotenv
import mysql.connector
import os

def connect():
    dbCon = mysql.connector.connect(
        host= os.getenv("HOST"),
        user= os.getenv("USER"),
        password= os.getenv("PASSWORD"),
        database= os.getenv("DB")
    )
    return dbCon

load_dotenv()