#!/usr/bin/env python
# dictionary example. For problem 9-12. YAYYYYY
import time, re, pickle, shelve

admin_name = "Rochambeau"
admin_pass = "RockPaperScissor"

db = {admin_name: admin_pass}

def newuser():
    """
    Adding functionality for 7.5f
    """
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        a_alpha_numeric_char = True
        alphanumeric = '^[\w]'
        for char in name:
            if re.search(alphanumeric, char) is None:
                a_alpha_numeric_char = False
        if not a_alpha_numeric_char:
            prompt = "Name contains illegal character(s). Try again: "
            continue
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')
    db[name] = pwd
    
def olduser():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    
    if name == admin_name and passwd == pwd:
        prompt = "Do you want to print accounts in file? Y/N: "
        account_print = raw_input(prompt).strip()[0].lower()
        if account_print == "y":
            """x = shelve.open("cool.db")
            try:
                x["awesome"] = {admin_name: admin_pass}
                blah = x["awesome"]
            finally: 
                x.close()
            print blah
            """
            with open("cool.pickle", "wb") as f:
                pickle.dump(db, f) # 9-12 b
            with open('cool.pickle', "rb") as g:
                print pickle.load(g)
            """for acc_name in db:
                f.write("%s : %s\n" % (acc_name, db[acc_name])) """ #9-12 a
    elif passwd == pwd:
        print ("Welcome back", name) 
    else:
        print ("login incorrect")
    
def showmenu():
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
                choice = raw_input(prompt).strip()[0].lower()
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
            elif time.time() - timestamp[0] <=  14400: # four hours in seconds
                pretty_timestamp = time.asctime(time.localtime(timestamp[0]))
                print("You have already logged in at", pretty_timestamp)
            else:
                timestamp[0] = time.time()
        if choice == "r":
            if db:
                db_name = raw_input("Please enter the user name you want to delete: ")
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
