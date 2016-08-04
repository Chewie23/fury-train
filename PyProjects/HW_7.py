#!/usr/bin/env python
"""
13-20 d. 
__radd__ is the "magic" method of allowing addition of objects as a SECOND argument; 
practically speaking, it allows an object to be on the RIGHT side of the "+" operator to be added to a corresponding argument. 
The object placement normally defaults to the LEFT side if using __add__. We do NOT need to use it since as long as 
a class object is on the left side, we can just simply use __add__. But if you HAVE to have a class object 
on the right side of the "+" operator, then __radd__ is needed.
"""

class Time60(object):
    """
    Time60 - track hours and minutes
    """
    
    def __init__(self, hr, min = 0, *time_tup, **time_dict): #13-20 a, c
        """
        Time60 initializer - takes hours and minutes
        """
        if time_tup: #13-20 c. Allows tuple input
            self.hr, self.min = time_tup
        elif time_dict: #13-20 c. Allows dictionary input
            self.hr  = time_dict["hr"]
            self.min = time_dict["min"]
        elif isinstance(hr, basestring): #13-20 c. Allows string input
            try:
                time_list = hr.split(":") 
                self.hr = time_list[0]
                self.min = time_list[1]
            except ValueError, IndexError:
                print "Invalid time string"        
        else: #13-20 a. Allows 2 arguments
            self.hr = hr
            self.min = min
        
        try:
            self.hr = int(self.hr) 
        except ValueError:
            print "Invalid value for hour position"
        try:
            self.min = int(self.min)
        except ValueError:
            print "Invalid value for minute position"
    
    def __str__(self):
        """
        Time60 - string representation
        """
        return "%02d:%02d" % (self.hr, self.min) #13-20 b. Allows "10:05" printing

    def __repr__(self): #13-20 e. Returns string
        return __str__(self)
    
    def __add__(self, other):
        """
        Time60 - overloading the addition operator
        """
        MIN_IN_HR = 60
        HR_IN_DAY = 24
        
        self.added_hr = self.hr + other.hr
        self.added_min = self.min + other.min
        
        
        if self.added_min // MIN_IN_HR > 0:
            self.added_hr += (self.added_min // MIN_IN_HR)
            self.added_min = (self.added_min % MIN_IN_HR)
         
        if self.added_hr // HR_IN_DAY > 0:
            self.added_hr = (self.added_hr % HR_IN_DAY)
        
        return self.__class__(self.added_hr, self.added_min) #13-20 f; sexagesimal operations
        
    def __iadd__(self, other):
        """
        Time60 - overloading in-place addition
        """
        self.hr += other.hr
        self.min += other.min
        return self
        
time_a = Time60(9,30)
time_b = Time60(hr = 14, min = 45)
time_c = Time60("8:55")
time_d = Time60(*(10, 30))
time_e = Time60(**{"hr": 8, "min": 45})
print "%s + %s = %s" % (time_a, time_b, time_a + time_b)
print "%s + %s = %s" % (time_c, time_d, time_c + time_d)

print time_a
print time_b
print time_c
print time_d
print time_e
"""Output
09:30 + 14:45 = 00:15
08:55 + 10:30 = 19:25
09:30
14:45
08:55
10:30
08:45
"""

#-------------------------------------------------------------------------------
#14-4 and problem 9, HW 7
import os
import subprocess #problem 9, HW 7
def opsys():
    os.system("cat cool.txt")
    os.system("echo --------------------------------------------------")
    subprocess.call("cat cool.txt | head -n 5", shell = True) #Problem 9, HW 7
opsys()
"""Output
1
2
3
4
5
6
7
8
9
0
---------------------------------------------------
1 #Problem 9, HW 7
2
3
4
5

"""
#-------------------------------------------------------------------------------
#15-14
import re

def month_find_list(line):
    line_elem = line.split(" ")
    month_list = []
    for n in line_elem:
        favorite_months = re.match(r"[1][0-2]", n) #the pattern to search for last three months
        if favorite_months:
            month_list.append(favorite_months.group())
    return month_list
line = "1 2 3 4 5 6 7 8 9 10 11 12"
print month_find_list(line)
"""Output
['10', '11', '12']
"""
#-------------------------------------------------------------------------------
#16-11
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