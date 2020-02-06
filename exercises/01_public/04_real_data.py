# Usage:
# 1) export FLASK_APP=build_a_flask_api.py
# 2) export FLASK_ENV=development
# 3) flask run --port 8081
# * To make it available to external IPs, execute it with the parameter: --host=0.0.0.0

from flask import Flask
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

def create_connection(db_file):
  """ create a database connection to the SQLite database
      specified by the db_file
  :param db_file: database file
  :return: Connection object or None
  """
  conn = None
  try:
      conn = sqlite3.connect(db_file)
  except Error as e:
      print(e)

  return conn

@app.route('/')
def hello_world():
  return 'Hello, World!'
