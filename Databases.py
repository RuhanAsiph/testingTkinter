from tkinter import *
import sqlite3

main = Tk()
main.title("Database")
main.geometry("400x400")

#creating a database or connecting to one
con = sqlite3.connect('address_book.db')

#creating a cursor
c = con.cursor()

#Tables
'''
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""") '''
#function to delete a Record
def delete():
    #creating a database or connecting to one
    con = sqlite3.connect('address_book.db')
    #creating a cursor
    c = con.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    delete_box.delete(0, END)


    #closing connection
    con.close()


#defining submit function
def submit():
    #creating a database or connecting to one
    con = sqlite3.connect('address_book.db')
    #creating a cursor
    c = con.cursor()

    #inserting data into tables
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address':address.get(),
                'city': city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()
                })

    #commiting changes
    con.commit()
    #closing connection
    con.close()
                
    #clearing the text boxes after we hit submit
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#defining query function
def query():
    #creating a database or connecting to one
    con = sqlite3.connect('address_book.db')
    #creating a cursor
    c = con.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)
    #Loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) +"\n"

    query_label = Label(main, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)
    
    #commiting changes
    con.commit()
    #closing connection
    con.close()


#entries
f_name = Entry(main, width=30)
f_name.grid(row=0,column=1, padx=20)
l_name = Entry(main, width=30)
l_name.grid(row=1,column=1, padx=20)
address = Entry(main, width=30)
address.grid(row=2,column=1, padx=20)
city = Entry(main, width=30)
city.grid(row=3,column=1, padx=20)
state = Entry(main, width=30)
state.grid(row=4,column=1, padx=20)
zipcode = Entry(main, width=30)
zipcode.grid(row=5,column=1, padx=20)
delete_box = Entry(main, width=30)
delete_box.grid(row=9, column=1)


#entries label
f_name_label = Label(main, text="First Name")
f_name_label.grid(row=0, column = 0)
l_name_label = Label(main, text="Last Name")
l_name_label.grid(row=1, column = 0)
address_label = Label(main, text="Address")
address_label.grid(row=2, column = 0)
city_label = Label(main, text="City")
city_label.grid(row=3, column = 0)
state_label = Label(main, text="State")
state_label.grid(row=4, column = 0)
zipcode_label = Label(main, text="Zipcode")
zipcode_label.grid(row=5, column = 0)
delete_box_label = Label(main, text="DELETE ID")
delete_box_label.grid(row=9, column=0)

#creating submit button
submit_btn = Button(main, text="Add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=1, padx=10, ipadx=104)

#creating a query button
queryButton = Button(main, text="Show Records", command=query)
queryButton.grid(row=7, column=0, columnspan=2, pady=1, padx=10, ipadx=137)

#creating a delete button
deleteButton = Button(main, text="Delete a record", command=delete)
deleteButton.grid(row=10, column=0, columnspan=2, pady=1, padx=10, ipadx=132)


#commiting changes
con.commit()

#closing connection
con.close()

main.mainloop()
