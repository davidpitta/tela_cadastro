import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')
database = os.environ.get('database')

cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)

cnx.close()
