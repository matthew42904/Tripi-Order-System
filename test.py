import sqlite3
from sqlite3 import Error
import time


try:
    conn = sqlite3.connect('./Tripi.db')
except Error as e:
    print(e)

c = conn.cursor()

one = str(input(""))

c.execute("UPDATE tripi SET TripiCode = '7777' WHERE item = 'pepsi'")
