import sqlite3
from sqlite3 import Error
import time


try:
    conn = sqlite3.connect('./Tripi.db')
except Error as e:
    print(e)

c = conn.cursor()

def make_table():
    try:
        # make table: 
        c.execute("""CREATE TABLE tripi (manufacture text, item text,TripiCode text)""")
        conn.commit()
        print("done")
        print()
    except Error as e:
        print(e)
        print("There was a error. Contact admin(Matthew Bakken)")


def new_item():
        while True:
            prod_1_manufature = str(input("Manufature Name: "))
            if prod_1_manufature == "":
                return
            prod_1_item = str(input("Item Name: "))
            if prod_1_item == "":
                return
            prod_1_TripiNumber= str(input("Tripi Number: "))
            if prod_1_TripiNumber == "":
                return
            #add to tripi with a input: 
            c.execute("INSERT INTO tripi VALUES (?, ?, ?)", (prod_1_manufature, prod_1_item, prod_1_TripiNumber))

            conn.commit()
            again = str(input("another? y/n: "))
            if again == "n":
                return
            else:
                return

def Manufature_lookup():
    pass

def item_lookup():
    pass

def tripinum_lookup():
    pass

def lookup_item():
    chose = str(input("""
                    1 - search by Manufature name
                    2 - search by Item name
                    3 - search by Tripi number
                    enter to go back
                    selected:  """))
        
    if chose == "1":
        Manufature_lookup()
    elif chose == "2":
        item_lookup()
    elif chose == "3":
        tripinum_lookup()
    else:
        return


while True: 
    chose = str(input("""
                1 - make table
                2 - new item
                3 - item lookup
                m - TBD
                e or enter - exit
                selected:  """))
    
    if chose == "1":
        make_table()
    elif chose == "2":
         new_item()
    elif chose == "3":
         lookup_item()
    elif chose == "m":
        print("you tried to go to a secret place but it failed. maybe one day. maybe one day hehehe")
        print()
    elif chose == "e":
        print("Have a good day :)")
        time.sleep(2)
        exit()
    else:
        print("Have a good day :)")
        time.sleep(3)
        exit()





# add to tripi with a pepsi manufature test item and a item number of 15699: 
#c.execute("""INSERT INTO tripi VALUES ("pepsi",'test5', "15669")""")



#c.execute("""SELECT * FROM tripi WHERE manufacture='pepsi'""")

#print(c.fetchall())


conn.close()