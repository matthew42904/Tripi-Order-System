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
        c.execute("""CREATE TABLE tripi (manufacture text, item text,TripiCode integer, quanity integer)""")
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
            prod_1_TripiNumber= int(input("Tripi Number: "))
            if prod_1_TripiNumber == "":
                return
            prod_1_quanity= int(input("minumum quanity: "))
            if prod_1_quanity == "":
                return
            #add to tripi with a input: 
            c.execute("INSERT INTO tripi VALUES (?, ?, ?, ?)", (prod_1_manufature, prod_1_item, prod_1_TripiNumber, prod_1_quanity))

            conn.commit()
            again = str(input("another? y/n: "))
            if again == "n":
                return
            else:
                pass

def Manufature_lookup():
    while True:
        manlook = str(input("enter a Manufature: "))
        c.execute("SELECT * FROM tripi WHERE manufacture=?", (manlook, ))
        records = c.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        print()
        for row in records:
            print("Manufature name: ", row[0])
            print("Item name: ", row[1])
            print("Tripi number: ", row[2])
            print("minumum quanity: ", row[3])
            print("\n")

        again = str(input("another? y/n: "))
        if again == "n":
            return
        else:
            pass

def item_lookup():
    while True:
        manlook = str(input("enter a Item: "))
        c.execute("SELECT * FROM tripi WHERE item=?", (manlook, ))
        records = c.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        print()
        for row in records:
            print("Manufature name: ", row[0])
            print("Item name: ", row[1])
            print("Tripi number: ", row[2])
            print("minumum quanity: ", row[3])
            print("\n")
        again = str(input("another? y/n: "))
        if again == "n":
            return
        else:
            pass

def tripinum_lookup():
    while True:
        manlook = int(input("enter a Item: "))
        c.execute("SELECT * FROM tripi WHERE TripiCode=?", (manlook, ))
        records = c.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        print()
        for row in records:
            print("Manufature name: ", row[0])
            print("Item name: ", row[1])
            print("Tripi number: ", row[2])
            print("minumum quanity: ", row[3])
            print("\n")
        again = str(input("another? y/n: "))
        if again == "n":
            return
        else:
            pass

def lookup_item():
    chose = str(input("""
                1 - search by Manufature name
                2 - search by Item name
                3 - search by Tripi number
                4 - return to home
                selected:  """))
        
    if chose == "1":
        Manufature_lookup()
    elif chose == "2":
        item_lookup()
    elif chose == "3":
        tripinum_lookup()
    elif chose == "4":
        return
    else:
        return

def remove_item():
    while True:
        num = int(input("""
        enter the tripi number of the item you want removed
        you entered:    """))
        
        c.execute("DELETE from tripi where TripiCode=?", (num, ))
        conn.commit()
        again = str(input("another? y/n: "))
        if again == "n":
            return
        else:
            pass

def editor_tripi_item():
    one = int(input("new tripi number: "))
    two = str(input("item name: "))
    c.execute("UPDATE tripi SET TripiCode = ? WHERE item = ?", (one, two, ))
    conn.commit()
    return

def editor_item_tripi():
    one = str(input("new item name: "))
    two = int(input("tripi number: "))
    c.execute("UPDATE tripi SET item = ? WHERE TripiCode = ?", (one, two, ))
    conn.commit()
    return

def editor_tripi_tripi():
    one = int(input("new tripi number: "))
    two = int(input("old tripi number: "))
    c.execute("UPDATE tripi SET TripiCode = ? WHERE TripiCode = ?", (one, two, ))
    conn.commit()
    return

def editor_quanity_tripi():
    one = int(input("new quanity number: "))
    two = int(input("tripi number: "))
    c.execute("UPDATE tripi SET quanity = ? WHERE TripiCode = ?", (one, two, ))
    conn.commit()
    return

def editor():
    chose = str(input("""
                1 - edit tripi number by item name
                2 - edit item name by tripi number
                3 - edit tripi number with tripi number
                4 - edit quanity with tripi number
                5 - return to home
                selected:  """))
        
    if chose == "1":
        editor_tripi_item()
    elif chose == "2":
        editor_item_tripi()
    elif chose == "3":
        editor_tripi_tripi()
    elif chose =='4':
        editor_quanity_tripi()
    elif chose == "5":
        return
    else:
        return

def tripi_order():
    import os 
    try:
        os.remove("tripi_numbers.png")
    except:
        print("there was no order")
    from PIL import Image, ImageDraw, ImageFont
    import time
    img = Image.open("blank.png")

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 18)

    import itertools
    for i in itertools.count(start=0):
        enter = str(input("item or exit to exit: "))
        if enter == "exit":
            break
        c.execute("SELECT TripiCode FROM tripi WHERE item=?", (enter, ))
        records = c.fetchall()
        for item in records:
            res = [item[0] for item in records] 
            draw.text((0,i*18), str(res[0]), (0,0,0), font=font)
            img.save("tripi_numbers.png")

while True: 
    chose = str(input("""
                1 - make table
                2 - new item
                3 - item lookup
                4 - remove items
                5 - number of items you have in you book
                6 - editor (HARD TO USE!!!)
                7 - push changes (NOT USED AT THIS TIME)
                8 - make a order (IF ANY ISSUES CONTACT ME)
                c - my contact info
                m - TBD
                e or enter - exit
                selected:  """))
    
    if chose == "1":
        make_table()
    elif chose == "2":
         new_item()
    elif chose == "3":
         lookup_item()
    elif chose == "4":
        remove_item()
    elif chose == "5":
        c.execute("SELECT * FROM tripi")
        records = c.fetchall()
        print()
        print("You have " + str(len(records)) + " In your book")
    elif chose == "6":
        editor()
    elif chose == '7':
        print("not used at this time")
    elif chose == '8':
        tripi_order()
    elif chose == "c":
        print()
        print("name: Matthew Bakken")
        print("email: matthew42904@gmail.com")
        print("discord: @m451224")
        print()
    elif chose == "m":
        print()
        print("just wanted to say keep looking at the possitive in life and put behind the negatives.")
        print("you will get through the hard times it will just take time.")
        print("you always have your team there for you when you need someone to talk to.")
        print("                                     😊")
        print()
    elif chose == "e":
        print("Have a good day :)")
        conn.close()
        time.sleep(2)
        exit()
    else:
        print("Have a good day :)")
        conn.close()
        #time.sleep(3)
        exit()