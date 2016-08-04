#I still wanna tackle this!
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6)

messages = inbox.Items
message = messages.GetLast()
body_content = message.body_content
print (body_content)

"""STACK OVERFLOW ANSWER THAT I LIKE:
Checking it there was something like 2000 unread mails to block and 4000 spam mails to block too. Of course that is a function to be automatized and I looked for a good solution for me. What I did:

[1] Used python IMAP to connect to Exchange server [2] Used beatifulsoup (python) to parse the href values inside the email [3] After that send a email 'thanking' the user for its collaboration (very important)

Three days after my boss thanked me for the great effort I was doing answering all the e-mails and that we got compliments. Because NOW we are answering back the customers. (not me the script)

Ok. now lets do a plan

    Check the imap python module [1], and after take one tutorial using ssl imap4 [4]
    Decide What is best for YOUR problem? Download the emails (pop3) or search and browse it at server (IMAP).
    CHECK if you can connect using the protocols IMAP4 or POP3 Before, exchange is buggy in this part please check this bug report too [3]
    Ok, you are sure you can connect using IMAP4 or POP3, now fetch one message and parse it with beatiful soup or lxml. (my case I looked for href and 'mailto:')
    Do a nice message using the field 'from:' the email making it personal
    PROFIT

[1] google it imap python

[2] google it BeautifulSoup python

[3] http://support.microsoft.com/kb/296387

[4] http://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/

Sorry but I had to give the google urls because of my low score.

I hope this answer give you some good pointers to your solution. Of course you can make it more hax0r using lxml, sending the data to a DB. But after you connect and start manipulating you can do anything :)
"""