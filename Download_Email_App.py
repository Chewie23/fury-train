import poplib
import StringIO, rfc822
import string, random

def download_random_mail(server_address, user, password):
    server = poplib.POP3_SSL(server_address) #connection to a server
    server.user(user)
    server.pass_(password) #login

    resp, items, octets = server.list()

    # download a random message
    id, size = string.split(random.choice(items))
    resp, text, octets = server.retr(id)

    text = string.join(text, "\n")
    file = StringIO.StringIO(text)

    message = rfc822.Message(file)

    return (message, message.items())
    
user = "testingforpythoncs21b"
password = raw_input("Enter your password: ")
server_address = "pop.mail.yahoo.com"

message, message_list = download_random_mail(server_address, user, password)

for k, v in message_list:
    print k, "=", v

print message.fp.read()