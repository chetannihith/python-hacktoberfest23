# Incomplete program

from tkinter import *
from PIL import ImageTk, Image
import sqlite3 as sql

root = Tk()
root.title('Slider')
#root.iconbitmap()
root.geometry("640x480")

# Create or connect to a database
conn = sql.connect("address.db")
# Cursor
cur = conn.cursor()

# Creating table

# cur.execute("""CREATE TABLE address(
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode text
    
# )""")

def submit():
    # Create or connect to a database
    conn = sql.connect("address.db")
    # Cursor
    cur = conn.cursor()  

    # Insert the data
    cur.execute("INSERT INTO addresses VALUES (:nam, :lst, :add, :cty, :ste, :zip)")
    {
        'nam':nam.get(),
        'lst':lst.get(),
        'add':add.get(),
        'cty':cty.get(),
        'ste':ste.get(),
        'zip':zip.get()
    }

    #Commit Changes
    conn.commit()
    # Close connections
    conn.close()

    #clear text boxes
    nam.delete(0,END)
    lst.delete(0,END)
    add.delete(0,END)
    cty.delete(0,END)
    ste.delete(0,END)
    zip.delete(0,END)

def query():
    # Create or connect to a database
    conn = sql.connect("address.db")
    # Cursor
    cur = conn.cursor() 


    #Commit Changes
    conn.commit()
    # Close connections
    conn.close()



# Creating text box
nam = Entry(root, width=10)
nam.grid(row=0, column=1, padx=20)
lst = Entry(root, width=10)
lst.grid(row=1, column=1, padx=20)
add = Entry(root, width=10)
add.grid(row=2, column=1, padx=20)
cty = Entry(root, width=10)
cty.grid(row=3, column=1, padx=20)
ste = Entry(root, width=10)
ste.grid(row=4, column=1, padx=20)
zip = Entry(root, width=10)
zip.grid(row=5, column=1, padx=20)

Label(root, text="First Name").grid(row=0, column=0)
Label(root, text="last Name").grid(row=1, column=0)
Label(root, text="address").grid(row=2, column=0)
Label(root, text="city").grid(row=3, column=0)
Label(root, text="state").grid(row=4, column=0)
Label(root, text="zipcode").grid(row=5, column=0)

btn = Button(root, text="Add Data", command=submit).grid(row=6 ,column=0, columnspan=2, pady=10 ,padx=10, ipadx=100)

qbtn = Button(root, text="Show Recocrd", command=query).grid(row=7 ,column=0, columnspan=2, pady=10 ,padx=10, ipadx=137)

#Commit Changes
conn.commit()

# Close connections
conn.close()

root.mainloop()
