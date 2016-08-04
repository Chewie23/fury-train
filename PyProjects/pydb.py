"""
7. (25) (databases) Find (and download if necessary) a database system (choose relational/SQL or non-relational/NoSQL not both), and get it up and running. Find a Python adapter for your database, 
research it, and connect to it via Python. 
Create a simple Python app that that manages employee names and employee IDs. The app should let users add, display, update, and remove employee entries (CRUD basically, i.e., create, read, update, delete). 
You can choose to create a command-line or web version.
Suggested RDBMSs: SQLite (comes w/Python), MySQL, PostgreSQL, Gadfly (pure Python)
Suggested NoSQL databases: MongoDB, CouchDB, Google Cloud Datastore (via App Engine)
"""
#need to test relentlessly. Or once or twice. Whatever.
import sqlite3

conn = sqlite3.connect("cool.sqlite")
print "Opened database successfully"

#conn.execute("CREATE TABLE company(ID, Name)")

employee_list = [
    ('01', 'Pat Bateman'), 
    ('02', 'Axel Lenz'), 
    ('03', 'Chris Coar')
    ]

#conn.executemany("INSERT INTO company(ID, Name) values(?, ?)", employee_list) 

def add_employee(ID, emp_name):
    data = [ID, emp_name]
    conn.execute("INSERT INTO company(ID, Name) VALUES (?, ?)", data)

def fetch_info():
    cursor = conn.execute("SELECT ID, Name from COMPANY")
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]      

def update_info(ID, emp_name):
    data = [ID, emp_name]
     conn.execute("UPDATE company SET ID=? Name=?", data) 

def delete_user(ID, emp_name):
    date = [ID, emp_name]
    try:
        conn.execute("DELETE FROM company WHERE ID=? Name=?", data)
    except ValueError:
        print "Error. Information does not exist"
    

add_employee('04', 'Craig') 

fetch_info()        
conn.commit()

conn.close()