"""
TODO:
- Make a GUI/Drop down to select prefilled fields
- This is made for walkups ONLY. No real flexibility in changing function/different variations

"""

"""
To see fields, go export the ticket to XML!
"""

from jira import JIRA
import pickle
import warnings
import getpass
warnings.filterwarnings("ignore") #this is here to ignore the "unsecure" warnings

URL2 = 'https://jira.rim.net/'

#below saves user and password if not already logged in already
#Don't know if this is kosher or not? There has to be a better way?
try:
    with open(r"cred.dat", "rb") as f:
        credentials = pickle.load(f)
except IOError:
    with open(r"cred.dat", "wb") as f:
        username = raw_input("Please enter username: ")
        password = getpass.getpass("Please enter password: ") #hides password from being seen!
        credentials = {username: password}
        pickle.dump(credentials, f)

if credentials:
    for key in credentials:
        username = key
        password = credentials[key]

options = {
    'server': URL2,
    'verify': False
}

ticket = JIRA(options, basic_auth=(username, password))

location = "GOOD "

usr_sum = raw_input("Please enter summary of the issue: ")

issue_sum = location + usr_sum

#creates ticket
new_issue = ticket.create_issue(project = 'WO',
                                summary = issue_sum,
                                description = issue_sum,
                                assignee = {'name': username},
                                reporter = {'name': username},
                                issuetype = {'name':'Request'},
                                customfield_14135 = {'value':'End User Services', 'child':{'value':'IT Regional Support'}},
                                customfield_12030 = {'value': 'Unplanned - Work Order'},
                                
                              )

#adding comment               
ticket.add_comment(new_issue, issue_sum)

#Transition ID: Selected = '11', Start Work = '31, Complete = '101'
work_flow_to_close = ['11', '31']
complete = '101'

#workflow to close ticket
for status in work_flow_to_close:
    ticket.transition_issue(new_issue, transition = status)

#actually closes ticket with resolution as complete ({'id': '6'} is the exact number)!
ticket.transition_issue(new_issue, transition = complete, resolution = {'id': '6'})