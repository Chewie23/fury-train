# coding: utf-8 
"""
Problems:

6.  (15) 9-12 (users & passwords III)

"""
import operator
import random
import profile  #made with pure Python, creates a lot of overhead for profiled program, 
                #but useful if trying to extend the profiler in some way

import cProfile #a C extension, with reasonable overhead. Good for long running programs

import hotshot  #another C extension, limits overhead but increases post-process time. 
                #Creates an object of "Profile" to start the profile of the script

def pass_tuple_in(tup, *fxn):
    """
    problem 5
    pass in a tuple to multiple functions
    """
    return [func(*tup) for func in fxn]
#problem 11
profile.run("print pass_tuple_in((2, 10), random.randint, operator.add, operator.sub, operator.pow)")
print "###################################################################################################"
cProfile.run("print pass_tuple_in((2, 10), random.randint, operator.add, operator.sub, operator.pow)")

"""Output
[3, 12, -8, 1024]
         10 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(add)
        1    0.000    0.000    0.000    0.000 :0(pow)
        1    0.000    0.000    0.000    0.000 :0(random)
        1    0.004    0.004    0.004    0.004 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(sub)
        1    0.003    0.003    0.004    0.004 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_5.py:19(pass_tuple_in)
        1    0.000    0.000    0.008    0.008 profile:0(print pass_tuple_in((2, 10), random.randint, operator.add, 
                                                                                    operator.sub, operator.pow))
        0    0.000             0.000          profile:0(profiler)
        1    0.000    0.000    0.000    0.000 random.py:173(randrange)
        1    0.000    0.000    0.000    0.000 random.py:237(randint)


###################################################################################################
[7, 12, -8, 1024]
         9 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_5.py:19(pass_tuple_in)
        1    0.000    0.000    0.000    0.000 random.py:173(randrange)
        1    0.000    0.000    0.000    0.000 random.py:237(randint)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {operator.add}
        1    0.000    0.000    0.000    0.000 {operator.pow}
        1    0.000    0.000    0.000    0.000 {operator.sub}
"""

#-----------------------------------------------------------------------------------
def olduser():
    """
    9-12 a, b, c
    Making an admin account and printing it out to a file
    """
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
            x = shelve.open("cool.db") #9-12 c
            try:
                x["awesome"] = {admin_name: admin_pass}
                blah = x["awesome"] 
            finally: 
                x.close()
            print blah #proving that this is stored
            
            """with open("cool.pickle", "wb") as f:
                pickle.dump(db, f) #9-12 b
            with open('cool.pickle', "rb") as g:
                print pickle.load(g)""" # To prove that this is stored.
            """for acc_name in db:
                f.write("%s : %s\n" % (acc_name, db[acc_name])) """ #9-12 a
    elif passwd == pwd:
        print ("Welcome back", name) 
    else:
        print ("login incorrect")
        
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
Enter Choice: n

You picked: (n)
login desired: c
passwd: d

(N)ew User Login
(E)xisiting User Login
(Q)uit
(R)emove User
(S)how Users and Password
Enter Choice: e

You picked: (e)
login: Rochambeau
passwd: RockPaperScissor
Do you want to print accounts in file? Y/N: y

FILE CONTENTS: 9-12 a
a : b
c : d
Rochambeau : RockPaperScissor

You picked: (e) 9-12 b
login: Rochambeau
passwd: RockPaperScissor
Do you want to print accounts in file? Y/N: y
{'Rochambeau': 'RockPaperScissor'} #proving that "Pickle" works

FILE CONTENTS: 9-12 b, to prove that "Pickle" works
(dp0
S'Rochambeau'
p1
S'RockPaperScissor'
p2
s.

You picked: (e) 9-12 c
login: Rochambeau
passwd: RockPaperScissor
Do you want to print accounts in file? Y/N: y
{'Rochambeau': 'RockPaperScissor'} #proving that "Shelve" works
"""
#-----------------------------------------------------------------------------------
def calculator():
    """
    9-14
    Gotta make a calculator program AND THEN add command line functionality
    Also have to write to disk and truncate when we print it out in cmd
    """
    import operator
    import sys
    
    #The series of try/except blocks are simply testing if there are enough valid inputs for the calc.
    try:
        x = str(sys.argv[1])
    except IndexError:
        return "Error. No input"
    
    if x == "print":
        with open("cool.txt", "r") as f:
            for line in f.read().splitlines():
                print line
        open("cool.txt", 'w').close()
        return None
    
    try:
        operation = sys.argv[2]
        y = sys.argv[3]
    except IndexError:
        return "Invalid Operation. Need more than one input"
    
    try:
        x = float(sys.argv[1])
        y = float(sys.argv[3])
    except ValueError:
        return "Invalid Input. Input(s) not number(s)"
    
    #Making a dictionary to reflect a given symbol with its correlated operation
    ops_dict = { "+": operator.add, "-": operator.sub, 
    "*": operator.mul, "/": operator.div, "^": operator.pow}
    try:
        math_sent = "\n%s %s %s\n" % (str(x), operation, str(y))
        result = "%.1f" % ops_dict[operation](x, y)
    except KeyError:
        return "Invalid Operation. Needs an operator symbol"
    
    with open("cool.txt", "a") as f:
            f.write(math_sent)
            f.write(result)
    return result

result = calculator()
if result is not None:
    print result
"""Output
PS C:\Users\achu\Desktop\Misc> python HW_5.py 1 + 2
3.0
PS C:\Users\achu\Desktop\Misc> python HW_5.py 4 ^ 2
16.0
PS C:\Users\achu\Desktop\Misc> python HW_5.py 5 * 7
35.0
PS C:\Users\achu\Desktop\Misc> python HW_5.py 2 - 4
-2.0
PS C:\Users\achu\Desktop\Misc> python HW_5.py 2 / 4
0.5
PS C:\Users\achu\Desktop\Misc> python HW_5.py print

1.0 + 2.0
3.0
4.0 ^ 2.0
16.0
5.0 * 7.0
35.0
2.0 - 4.0
-2.0
2.0 / 4.0
0.5
PS C:\Users\achu\Desktop\Misc> python HW_5.py print
PS C:\Users\achu\Desktop\Misc>
"""
#-----------------------------------------------------------------------------------    
def search_file_byte(byte_str, filename):
    """
    9-18
    searches file for specified byte in a given file
    file contents:
    He that is proud eats up himself: pride is
    his own glass, his own trumpet, his own chronicle.
    """  
    try:
        byte_num = int(byte_str)
    except ValueError:
        return "Invalid Input"
    byte_char = chr(byte_num)
    count = 0
    with open(filename, "r") as f:
        while True:
            char = f.read(1)          # read by character
            if char == byte_char:
                count += 1
            if not char: 
                break
    return "%d instances of byte %r, or in Python %r" % (count, byte_str, byte_char)

"""filename = raw_input("Please type in your file (including extension): ")
byte_str = raw_input("Please put a byte number 0-255: ")
print search_file_byte(byte_str, filename)
"""
"""Output
Please type in your file (including extension): Agamemnon.txt
Please put a byte number 0-255: 101
6 instances of byte '101', or in Python 'e'
"""

def make_byte_file(filename, byte_num, instance, size):
    """
    9-19
    Sister function to 9-18.
    Makes a file, adds in number of bytes and specified number of a specific byte
    """
    from random import randint
    
    with open(filename, "w") as f:
        for i in range(0, instance):
            f.write(chr(byte_num))
        for n in range(0, size - instance):
            f.write(chr(randint(0, 255)))

filename = raw_input("Please enter a name of file: ")            
byte_str = raw_input("Please put a byte number 0-255: ")
byte_instances = raw_input("Please enter how many times the byte number appears: ")
file_size = raw_input("Please enter how big the file is: ")

try:
    byte_num = int(byte_str)
    instance = int(byte_instances)
    size = int(file_size)
except ValueError:
    print "Invalid Input"
    exit(0)

if instance > size:
    print "Invalid size. Size needs to be bigger than instances"
elif instance < 0 or size < 0:
    print "Invalid number"

"""
make_byte_file(filename, byte_num, instance, size)
print search_file_byte(byte_str, filename) #to confirm how many times it writes it out
"""
"""Output:
Please enter a name of file: seltzer.txt
Please put a byte number 0-255: 57
Please enter how many times the byte number appears: 45
Please enter how big the file is: 100
45 instances of byte '57', or in Python '9'
FILE CONTENTS:
999999999999999999999999999999999999999999999»êèüšnXlS›{
\{xpŒpöV¯qCftÃgfû„»Láqú+4‚Züõ«Ú;Õý
"""
#--------------------------------------------------------------------------------------------------
class LIFO(object):
    """
    13.8
    Literally a stack class. Need to create a push(), pop(), isempty() which chcks if empty and returns a Bool, 
    peek() which shows top of stack method.
    For fun.
    """
    def __init__(self, stack):
        self.stack = stack
    def push(self, item):
        self.stack.append(item)
    def pop_out(self):
        self.stack.pop()
    def isempty(self):
        if self.stack:
            return False
        return True
    def peek(self):
        return self.stack[len(self.stack) - 1]
        
cool_list = [1, 2, 3, 4, 5, 6]
another_list = [10, 11, "a", "b", "g"]

print "Unmodified list: ", cool_list
print "Unmodified list: ", another_list

x = LIFO(cool_list)
y = LIFO(another_list)
x.push(7)
x.push(10)
x.push(19)
y.push("abba")
y.push("baab")

print "Modified list: ", cool_list
print "Modified list: ", another_list

print x.peek()
print y.peek()
print x.isempty()
x.pop_out()
x.pop_out()
print x.peek()
print "Modified list: ", cool_list
"""Output
Unmodified list:  [1, 2, 3, 4, 5, 6]
Unmodified list:  [10, 11, 'a', 'b', 'g']
Modified list:  [1, 2, 3, 4, 5, 6, 7, 10, 19]
Modified list:  [10, 11, 'a', 'b', 'g', 'abba', 'baab']
19
baab
False
7
Modified list:  [1, 2, 3, 4, 5, 6, 7]
"""