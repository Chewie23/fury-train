import socket
import sys
import time

def HTTP_to_file(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + 1

    try:
        s.connect((address, port))
        print ("successful connection")
    except ValueError:
        pass
    s.send(b"GET / HTTP/1.1\r\n\r\n")

    with open("ran.txt", "wb") as f:
        while True:
            if time.time() > end_time:
                s.close()
                break
            buf = s.recv(4096)
            f.write(buf)
address = "google.com"
port = 80
HTTP_to_file(address, port)
print("done")
            
"""Output
successful connection
done

Output file:
HTTP/1.1 200 OK
Date: Sun, 06 Mar 2016 03:37:13 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See https://www.google.com/support/accounts/answer/151657?hl=en for more info."
Server: gws
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Set-Cookie: NID=77=Ds5rNHi4VdaqRPUY8k53ce3sNJ9ZDvRFpVvJ6y-0J2e_o7DCd9bwSeco064C1jijWIDWbRLUh_qlygp82zDgRAq_F8HM-5wWfouMleC_Kp-5XZjFxYGmpuVE8f30ufEE8VfcxVOfORL2Qw; expires=Mon, 05-Sep-2016 03:37:13 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

8000...Too long to print. Save trees.
"""