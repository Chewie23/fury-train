#!/usr/bin/env python
# dictionary example. For problem 7-5
import time

db = {}

def newuser():
    prompt = 'login desired: '
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = input('passwd: ')
    db[name] = pwd
    
def olduser():
    """
    9-12 a, b, c
    Making an admin account and printing it out to a file
    """
    import shelve
    #import pickle 9-12 b
    admin_name = "Rochambeau"
    admin_pass = "RockPaperScissor"

    db = {admin_name: admin_pass}
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    
    if name == admin_name and passwd == pwd:
        prompt = "Do you want to print accounts in file? Y/N: "
        account_print = raw_input(prompt).strip()[0].lower()
       if account_print == "y":
            #9-12 c
            x = shelve.open("cool.db") 
            try:
                x["awesome"] = {admin_name: admin_pass}
                blah = x["awesome"] 
            finally: 
                x.close()
            print blah #proving that this is stored
            #9-12 b
            """
            with open("cool.pickle", "wb") as f:
                pickle.dump(db, f) 
            with open('cool.pickle', "rb") as g:
                print pickle.load(g)  #To prove that this is stored.
            """ 
            #9-12 a
            """
            for acc_name in db:
                f.write("%s : %s\n" % (acc_name, db[acc_name])) 
            """ 
    elif passwd == pwd:
        print ("Welcome back", name) 
    else:
        print ("login incorrect")
  
def showmenu():
    time_limit = 14400 # four hours in seconds
    timestamp = []
    prompt = """
(N)ew User Login
(E)xisiting User Login
(Q)uit
(R)emove User
(S)how Users and Password
Enter Choice: """
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print ("\nYou picked: (%s)" % choice)
            if choice not in 'neqsr':
                print ("option invalid, try again")
            else:
                chosen = True
        if choice == "q": 
            done = True
        if choice == "n": 
            newuser()
        if choice == "e": 
            olduser()
            if not timestamp:
                timestamp.append(time.time())
            elif time.time() - timestamp[0] <= time_limit:
                pretty_timestamp = time.asctime(time.localtime(timestamp[0]))
                print("You have already logged in at", pretty_timestamp)
            else:
                timestamp[0] = time.time()
        if choice == "r":
            if db:
                db_name = input("Please enter the user name you want to delete: ")
                db.pop(db_name, None)
            else:
                print ("There are no users yet!")
        if choice == "s":
            if db:
                for name in db:
                    print ("name: %s, pass: %s /" % (name, db[name]))
            else:
                print ("There are no users yet!")
            
if __name__ == "__main__":
    showmenu()
"""Output
(N)ew User Login
(E)xisiting User Login
(Q)uit
(R)emove User
(S)how Users and Password
Enter Choice: n

You picked: (n)
login desired: a
passwd: b

(N)ew User Login
(E)xisiting User Login
(Q)uit
(R)emove User
(S)how Users and Password
Enter Choice: e

You picked: (e)
login: a
passwd: b
Welcome back a

(N)ew User Login
(E)xisiting User Login
(Q)uit
(R)emove User
(S)how Users and Password
Enter Choice: e

You picked: (e)
login: a
passwd: b
Welcome back a
You have already logged in at Sun Jan 24 17:54:09 2016

(N)ew User Login
(E)xisiting User Login
(Q)uit
(R)emove User
(S)how Users and Password
Enter Choice: s

You picked: (s)
name: a, pass: b /

(N)ew User Login
(E)xisiting User Login
(Q)uit
(R)emove User
(S)how Users and Password
Enter Choice: r

You picked: (r)
Please enter the user name you want to delete: a

(N)ew User Login
(E)xisiting User Login
(Q)uit
(R)emove User
(S)how Users and Password
Enter Choice: s

You picked: (s)
There are no users yet!

(N)ew User Login
(E)xisiting User Login
(Q)uit
(R)emove User
(S)how Users and Password
Enter Choice: q

You picked: (q)
"""