import sqlite3
from sqlite3 import Error


try:
    conn = sqlite3.connect('Tripi.db')
except Error as e:
    print(e)

c = conn.cursor()
while True: 
    prod_1_manufature = str(input("Manufature Name: "))
    prod_1_item = str(input("Item Name: "))
    prod_1_TripiNumber= str(input("Tripi Number: "))
    # add to tripi with a input: 
    c.execute("INSERT INTO tripi VALUES (?, ?, ?)", (prod_1_manufature, prod_1_item, prod_1_TripiNumber))

    conn.commit()



# make table: 
#c.execute("""CREATE TABLE tripi (manufacture text, item text,TripiCode text)""")

# add to tripi with a pepsi manufature test item and a item number of 15699: 
#c.execute("""INSERT INTO tripi VALUES ("pepsi",'test5', "15669")""")



#c.execute("""SELECT * FROM tripi WHERE manufacture='pepsi'""")

#print(c.fetchall())


conn.close()