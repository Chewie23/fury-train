import jira #may want to streamline this
from jira import JIRA
import pickle

URL = 'https://jiraqa.rim.net/'
URL2 = 'https://jira.rim.net/'

#below saves user and password if not already logged in already
try:
    with open(r"test_cred.dat", "rb") as f:
        credentials = pickle.load(f)
except IOError:
    with open(r"test_cred.dat", "wb") as f:
        username = raw_input("Please enter username: ")
        password = raw_input("Please enter password: ")
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

WO_num = 'WO-266574'

current_issue = ticket.issue(WO_num)

ticket.transition_issue(current_issue, transition = '101') #WORKS. YEAH MF'ERRRR. Closes the ticket
print "here"
"""
current_issue = ticket.issue(WO_num)
close_issue = ticket.transitions(current_issue)
print close_issue
print [(t['id'], t['name']) for t in close_issue]
"""
