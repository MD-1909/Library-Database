import mysql.connector #import the MySQL module

db = mysql.connector.connect(host = "localhost", user = "root", password = "password") #Replace the values with the username and password of your MySQL server
cur = db.cursor() #create cursor object
cur.execute("CREATE DATABASE IF NOT EXISTS library") #create master database
cur.execute("USE library") #select the database
cur.execute("CREATE TABLE IF NOT EXISTS books \n(ID INTEGER UNSIGNED NOT NULL PRIMARY KEY, Title VARCHAR(80), Author VARCHAR(80))") #create the table for books

insert_query = """INSERT INTO books\n(ID, Title, Author) VALUES (%s, %s, %s)"""
delete_query = """DELETE FROM books WHERE ID = %s"""
search_query1 = """SELECT * FROM books WHERE id = %s"""
search_query2 = """SELECT * FROM books WHERE title REGEXP %s"""
search_query3 = """SELECT * FROM books WHERE author REGEXP %s"""

def library():
    """The main function that implements all the services provided by the library application"""
    while True:
        cur.execute("SELECT ID FROM books")
        trials = cur.fetchall() #maintain a record of the rows present in the table. Is updated after every loop
        x = input("\nEnter the option corresponding to what you want to do:\n1: View table\n2: Search table\n3: Insert an entry\n4: Delete an entry\n5: Exit\n")
        try:
            x = int(x)
            pass
        except:
            print("\nInvalid option, please try again.") #in case the user enters a string which cannot be converted to integer type
            pass

        if x == 1: #to print the table
            cur.execute("SELECT * FROM books") #sql query to fetch entire table
            printer = cur.fetchall()
            print("\n(ID, Title, Author)")
            for x in printer:
                print(x)
            y = input("\nPress Enter to return to Main Menu.\n")
            y = y.lower()
            if y == "yes":
                pass
            else:
                pass

        elif x == 2: #to search for specific rows
            option = input("\nWhich parameter would you like to search for?\n1: ID\n2: Title\n3: Author\n")
            try:
                option = int(option)
                pass
            except:
                print("\nInvalid option, please try again.")
                pass
            if option == 1:
                idno = int(input("ID: "))
                cur.execute(search_query1, (idno,))
                printer = cur.fetchall()
                if printer:
                    print("\n(ID, Title, Author)")
                    for x in printer:
                        print(x)
                else:
                    print("\nNo records found.")
                y = input("\nPress Enter to return to Main Menu.\n")
                y = y.lower()
                if y == "yes":
                    pass
                else:
                    pass
            elif option == 2:
                title = input("Title: ")
                cur.execute(search_query2, (title,))
                printer = cur.fetchall()
                if printer:
                    print("\n(ID, Title, Author)")
                    for x in printer:
                        print(x)
                else:
                    print("\nNo records found.")
                y = input("\nPress Enter to return to Main Menu.\n")
                y = y.lower()
                if y == "yes":
                    pass
                else:
                    pass
            elif option == 3:
                author = input("Author: ")
                cur.execute(search_query3, (author,))
                printer = cur.fetchall()
                if printer:
                    print("\n(ID, Title, Author)")
                    for x in printer:
                        print(x)
                else:
                    print("\nNo records found.")
                y = input("\nPress Enter to return to Main Menu.\n")
                y = y.lower()
                if y == "yes":
                    pass
                else:
                    pass
            else:
                print("\nInvalid option, please try again.")
                pass
  
        elif x == 3: #to insert a new row
            print("\nEnter the data to be updated")
            idno = int(input("ID: "))
            title = input("Title: ") 
            author = input("Author: ")
            record = (idno, title, author)
            cur.execute(insert_query, record)
            db.commit()
            print("\nDo you want to view the table? (Y/N)")
            yn = input()
            yn = yn.lower()
            if yn == "y":
                cur.execute("SELECT * FROM books")
                printer = cur.fetchall()
                print("\n(ID, Title, Author)")
                for x in printer:
                    print(x)
                pass
            elif yn == "n":
                pass
            y = input("\nPress Enter to return to Main Menu.\n")
            y = y.lower()
            if y == "yes":
                pass
            else:
                pass

        elif x == 4: #to delete a row
            print("\nEnter ID Number of the entry to be deleted")
            idno = input("ID: ")
            y = int(idno)
            z = (y,)
            if z in trials: #check the record to see if the entered row exists
                cur.execute(delete_query, (idno,))
                db.commit()
                print("\nRecord deleted successfully.")
                print("\nDo you want to view the table? (Y/N)")
                yn = input()
                yn = yn.lower()
                if yn == "y":
                    cur.execute("SELECT * FROM books")
                    printer = cur.fetchall()
                    print("\n(ID, Title, Author)")
                    for x in printer:
                        print(x) 
                    pass
                elif yn == "n":
                    pass
            else:
                print("\nThe record does not exist.")
            y = input("\nPress Enter to return to Main Menu.\n")
            y = y.lower()
            if y == "yes":
                pass
            else:
                pass
            
        elif x == 5: #Exit the program
            print("\nThank you for using this service. Please visit again.")
            cur.close()
            return
        else:
            print("\nInvalid option, please try again.")
            pass

print("\nWelcome to the Library, what would you like to do?")
library()        