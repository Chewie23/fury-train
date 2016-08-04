#20-6
#!/usr/bin/env python

import cgi
from urllib import quote_plus
from string import capwords

header = "Content-Type: text/html\n\n"
url = "/cgi-bin/friends3.py"

errhtml = """<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT Type=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>"""

def showError(error_str):
    print header + errhtml % (error_str)
    
formhtml = """<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
<FORM ACTION="%s">
<B>Your Name:</B>
<INPUT TYPE=hidden NAME=action VALUE=edit>
<INPUT TYPE=text NAME=person VALUE="%s" SIZE=15>
<P><B>How many friends do you have?</B>
%s
<P><INPUT TYPE=submit></FORM></BODY></HTML>"""

fradio = '<INPUT TYPE=radio NAME=howmany VALUE="%s" %s> %s\n'

def showForm(who, howmany):
    friends = ""
    for n in [0, 10, 25, 50, 100]:
        checked = ""
        if str(n) == howmany:
            checked = "CHECKED"
        friends = friends + fradio % \
            (str(n), checked, str(n))
    print header + formhtml % (who, url, who, friends)
    
reshtml = """<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
<P>Click<A HREF="%s">here</A> to edit your data again.
</BODY></HTML>"""

def doResults(who, howmany):
    newurl = url + "?action=reedit&person=%s&howmany=%s"%\
        (quote_plus(who), howmany)
    print header + reshtml % (who, who, howmany, newurl)

def process():
    error = ""
    form = cgi.FieldStorage()
    print form
    
    if form.has_key("person"):
        who = capwords(form['person'].value)
    elif " " in form or "" in form: #error catching no name or blankspace
        error = "Please enter a valid name."
    else:
        who = "NEW USER"
    
    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        if form.has_key('action') and \
                form['action'].value == 'edit':
            error = "Please select number of friends."
        else:
            howmany = 0
            
    if not error:
        if form.has_key('action') and \
                form['action'].value != 'reedit':
            doResults(who, howmany)
        else:
            showForm(who, howmany)
    else:
        showError(error)
        
if __name__ == "__main__":
    process()
"""OUTPUT
See pictures attached

"""
#--------------------------------------------------------------------------------
# Problem 7, HW 9
import sqlite3

def create_table(conn):
    conn.execute("CREATE TABLE company(ID, Name)")

def initialize_table(conn, employee_list):
    conn.executemany("INSERT INTO company(ID, Name) values(?, ?)", employee_list) 

def add_employee(conn, ID, emp_name):
    data = [ID, emp_name]
    conn.execute("INSERT INTO company(ID, Name) VALUES (?, ?)", data)

def fetch_info(conn):
    cursor = conn.execute("SELECT ID, Name FROM company")
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]      

def update_info(conn, new_name, old_name): #logically, you don't change employee IDs
    conn.execute("UPDATE company SET Name=? WHERE Name=?", (new_name, old_name))
        
def delete_employee(conn, ID):
    for x in conn.execute("SELECT rowid FROM company WHERE ID=?", (ID,)):
        conn.execute("DELETE FROM company WHERE rowid=?", x)
        
conn = sqlite3.connect("cool.sqlite")
print "Opened database successfully"
    
employee_list = [
    ('01', 'Pat Bateman'), 
    ('02', 'Axel Lenz'), 
    ('03', 'Chris Coar')
    ]
create_table(conn)
initialize_table(conn, employee_list)
fetch_info(conn)
print "--------------------------------------------"
add_employee(conn, '04', 'Craig') 
fetch_info(conn)        
print "--------------------------------------------"
delete_employee(conn,'01')
fetch_info(conn)
print "--------------------------------------------"
update_info(conn, 'Alex Lenz', 'Axel Lenz')
fetch_info(conn)

conn.commit()
conn.close()

"""OUTPUT
Opened database successfully
ID =  01
NAME =  Pat Bateman
ID =  02
NAME =  Axel Lenz
ID =  03
NAME =  Chris Coar
--------------------------------------------
ID =  01
NAME =  Pat Bateman
ID =  02
NAME =  Axel Lenz
ID =  03
NAME =  Chris Coar
ID =  04
NAME =  Craig
--------------------------------------------
ID =  02
NAME =  Axel Lenz
ID =  03
NAME =  Chris Coar
ID =  04
NAME =  Craig
--------------------------------------------
ID =  02
NAME =  Alex Lenz
ID =  03
NAME =  Chris Coar
ID =  04
NAME =  Craig
"""
#--------------------------------------------------------------------------------
#Problem 8, HW 9
#database.py, to create db
from peewee import *
from datetime import datetime

DATABASE = "guestbook.db"
DATE = datetime.now().strftime("%H:%M - %d/%m/%y")
database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database

class Post(BaseModel):
    name = CharField()
    email = CharField(null=True)
    website = CharField(null=True)
    comment = TextField()
    date = DateTimeField()

def create_tables():
    database.connect()
    database.create_tables([Post])
    database.close()

create_tables()

database.connect()

post_one = Post.create(name="Pippin",
                       website="http://python.org",
                       comment="Check out Python for cool programming things!",
                       date=DATE)

post_two = Post.create(name="Merry",
                       website="https://www.wikipedia.org/",
                       comment="Wikipedia is one of the largest encyclopedia resources",
                       date=DATE)

# Close the database
database.close()

print("Created the database!")

#server.py, to run as a server
import http.server

PORT = 8123
HOST = "localhost"

server_address = (HOST, PORT)
cgi_server = http.server.CGIHTTPRequestHandler

httpd = http.server.HTTPServer(server_address, cgi_server)
print("Starting my web server on port {0}".format(PORT))

httpd.serve_forever()

#script.py, the actual guestbook
#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()
import re

from peewee import *
from datetime import datetime


DATABASE = "guestbook.db"
database = SqliteDatabase(DATABASE)

class BaseModel(Model):

    class Meta:
        database = database


class Post(BaseModel):
    name = CharField()
    email = CharField(null=True)
    website = CharField(null=True)
    comment = TextField()
    date = DateTimeField()

template_file = "index.html"


def display(content):
    """ Displays HTML within the template file

        Subsitutes "<!--INSERT CONTENT HERE-->" within the index file
        content = the HTML you wish to display
    """

    template_handle = open(template_file, "r")
    template_input = template_handle.read()
    template_handle.close()

    template_error = "There was a problem with the HTML template"

    sub_result = re.subn('content', content, template_input)
    if sub_result[1] == 0:
        raise Exception(template_error)

    print("Content-type: text/html")

    print()
    print(sub_result[0])


def guestbook():
    """ Retrieves the posts from the database and converts them to HTML
    """

    guestbook_post = ""
    for post in Post.select().limit(10).order_by(Post.date.desc()):
        guestbook_post += """<article class='post' role="article">
                                <div class='comment'>
                                    <p class='text'>
                                        {0}
                                    </p>
                                    <p class='date'>
                                        {1}
                                    </p>
                                </div>

                                <div class="details">
                                    <span class='name'>{2}</span>
                          """.format(post.comment, post.date, post.name)

        if post.email:
            guestbook_post += """<span class='email'>
                                    | <a href='mailto:{0}' tabindex="1">@</a>
                                </span>
                              """.format(post.email)

        if post.website and (post.website.startswith("http://") or
                             post.website.startswith("https://")):
            guestbook_post += """<span class='website'>
                                    | <a href='{0}' tabindex="1">WWW</a>
                                 </span>
                              """.format(post.website)

        elif post.website:
            guestbook_post += """<span class='website'>
                                    | <a href='http://{0}' tabindex="1">WWW</a>
                                 </span>
                              """.format(post.website)

        guestbook_post += """</div>
                             </article>

                             <hr>
                          """

    def visitor_counter():
        """ Displays the number of visitors to the website
            Currently executed each time the script is loaded (which is bad)
        """
        counter = open("counter.txt", "r")
        line = counter.readline()
        counter.close()

        if line == "":
            number = 1
        else:
            number = int(line) + 1

        counter = open("counter.txt", "w")
        counter.write(str(number))
        counter.close()

        if number == 1:
            visits = """
            <div id="counter">
                <p id="count">{0} visitor</p>
            </div>
            """.format(number)
        else:
            visits = """
            <div id="counter">
                <p id="count">{0} visitors</p>
            </div>
            """.format(number)

        return visits

    return guestbook_post + visitor_counter()


def create_post():
    """ Creates a post in the database depending on the form information submitted
    """
    try:
        comment = form["comment"].value
    except:
        comment = "I didn't enter a comment :("

    try:
        name = form["name"].value
    except:
        print("Content-type: text/html")
        print()
        print("You need to at least submit a name. \
              Please go back and try again!")
        raise SystemExit

    try:
        email = form["email"].value
    except:
        email = None

    try:
        website = form["website"].value
    except:
        website = None

    post = Post.create(
        comment=comment,
        name=form["name"].value,
        email=email,
        website=website,
        date=datetime.now().strftime("%H:%M - %d/%m/%y")
    )

form = cgi.FieldStorage()

try:
    key = form["key"].value
except:
    key = None

if key == "process":
    create_post()

display(guestbook())

"""OUTPUT
See pictures attached
"""