import sqlite3
from sqlite3 import Error
import time


try:
    conn = sqlite3.connect('./Tripi.db')
except Error as e:
    print(e)

c = conn.cursor()

c.execute("SELECT * FROM tripi")
records = c.fetchall()
print(len(records))