
from jira import JIRA
import pickle
import warnings
import getpass
warnings.filterwarnings("ignore") #this is here to ignore the "unsecure" warnings

URL2 = 'https://jira.rim.net/'

try:
    with open(r"user.bin", "rb") as f:
        username = pickle.load(f)
except IOError:
    with open(r"user.bin", "wb") as f:
        username = raw_input("Please enter username: ")
        pickle.dump(username, f)

password = getpass.getpass("Please enter password: ") #need to login everytime. HRMMM.

options = {
    'server': URL2,
    'verify': False
}

ticket = JIRA(options, basic_auth=(username, password))

def creating_logging_ticket(ticket, username_reporter, issue_sum):
    #creates ticket
    print "Creating ticket..."
    new_issue = ticket.create_issue(project = 'WO',
                                    summary = issue_sum,
                                    description = issue_sum,
                                    assignee = {'name': username},
                                    reporter = {'name': username_reporter},
                                    issuetype = {'name':'Request'},
                                    customfield_14135 = {'value':'End User Services', 'child':{'value':'IT Regional Support'}},
                                    customfield_12030 = {'value': 'Unplanned - Work Order'},                                
                                  )

    #adding comment               
    ticket.add_comment(new_issue, issue_sum)
    return new_issue

def open_ticket(ticket):
    usr_location = raw_input("""Please choose the location number the issue originated from 
(defaults to blank location)
[1] BlackBerry
[2] AtHoc
[3] Good Tech
[4] WatchDox
> """)

    if usr_location == "1":
        location = "BlackBerry - "
    elif usr_location == "2":
        location = "AtHoc - "
    elif usr_location == "3":
        location = "Good Tech - "
    elif usr_location == "4":
        location = "WatchDox - "
    else: 
        location = ""

    usr_sum = raw_input("Please enter summary of the issue: ")
    
    issue_sum = location + usr_sum
    who_is_reporting = raw_input("""Who is reporting the issue? 
[1] Yourself
[2] User who walked up
""")

    if who_is_reporting == "1":
        username_reporter = username
        return creating_logging_ticket(ticket, username, issue_sum)
    elif who_is_reporting == "2":
        username_reporter = raw_input("Please enter username of walkup: ")
        return creating_logging_ticket(ticket, username_reporter, issue_sum)

def close_ticket(ticket, issue):    

    #Transition ID: Selected = '11', Start Work = '31, Complete = '101'
    work_flow_to_close = ['11', '31']
    complete = '101'

    print "Closing ticket..."
    #workflow to close ticket
    for status in work_flow_to_close:
        ticket.transition_issue(issue, transition = status)

    #actually closes ticket with resolution as complete ({'id': '6'} is the exact number)!
    ticket.transition_issue(issue, transition = complete, resolution = {'id': '6'})

def open_close_ticket(ticket):
    new_issue = open_ticket(ticket)
    print new_issue
    close_ticket(ticket, new_issue)

def start():
    prompt = """
Please choose the option number you want:
(defaults to [3] Open AND Close ticket)
[1] Open Ticket
[2] Close Ticket
[3] Open AND Close ticket (after resolving ticketless walkups/calls)
[4] Quit
> """
    done = False
    while not done:     
        chosen = False
        while not chosen:
            try:
                usr_choice = raw_input(prompt)
            except (EOFError, KeyboardInterrupt):
                usr_choice = '4'
            if usr_choice == "":
                usr_choice = '3'
            print ("\nYou picked: (%s)" % usr_choice)
            if usr_choice not in '1234':
                print ("Option invalid, try again")
            else:
                chosen = True
        if usr_choice == "4":
            done = True
        elif usr_choice == "1":
            new_issue = open_ticket(ticket)
            print "The WO is: ", new_issue
        elif usr_choice == "2":
            WO_num = raw_input("""Please enter your WO number (numbers only! No 'WO'!): 
Ex. For WO-123456, enter '123456'
> """)
            WO = "WO-" + WO_num
            try:
                issue_to_close = ticket.issue(WO)
            except:
                print "Please type only numbers!"
                continue
            ticket.assign_issue(issue_to_close, username) #changes assignee to username
            want_to_comment = raw_input("Do you want to add a comment? Y/N: ")
            if want_to_comment in ["Y", "y", "yes", "Yes"]:
                comment = raw_input("Please enter a short description on how you resolved the issue: ")
                update_issue_comment = ticket.add_comment(issue_to_close, comment)
            close_ticket(ticket, issue_to_close)
            print "Closed " + WO
        else:
            open_close_ticket(ticket)
    print "Goodbye"
start()
