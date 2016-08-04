def num_to_str(num):
    """
    6.8
    convert numeric value to read as string
    ex. 89 -> "eighty-nine"
    """
    ones_db = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    teens_db = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 
                15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
    tens_db = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
    spelled = []
    
    for n in [1000, 100, 10, 1]:
        if n == 1000 and num // n > 0:
            spelled.extend((ones_db[num // n], "thousand"))
        elif n == 100 and num // n > 0:
            spelled.extend((ones_db[num // n], "hundred"))
        elif n == 10 and num // n >= 2:
            spelled.append(tens_db[num // n])
        elif n == 10 and num // n == 1:
            spelled.append(teens_db[num])
            return ' '.join(spelled)
        elif n == 1 and num // n > 0:
            spelled.append(ones_db[num // n])
        num = num % n
    return ' '.join(spelled)
print(num_to_str(918))
print(num_to_str(849))
print(num_to_str(89))
"""Output
nine hundred eighteen
eight hundred forty nine
eighty nine
"""

def newuser():
    """
    Adding functionality for 7.5f
    """
    import re
    
    db = {}
    prompt = 'login desired: '
    while True:
        name = input(prompt)
        an_alpha_numeric_char = True
        alphanumeric = '^[\w]'
        for char in name:
            if re.search(alphanumeric, char) is None:
                an_alpha_numeric_char = False
        if not an_alpha_numeric_char:
            prompt = "Name contains illegal character(s). Try again: "
            continue
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = input('passwd: ')
    db[name] = pwd
"""output
(N)ew User Login
(E)xisiting User Login
(Q)uit
(R)emove User
(S)how Users and Password
Enter Choice: n

You picked: (n)
login desired: SDFSD#$##$%SDGFSGS
Name contains illegal character(s). Try again: q
passwd: q
"""

def rot13(sentence):
    """
    7.10
    create an encryption that is a cypher that 
    moves the letter 13 places
    Ex. a = n; b = o; z = m; w = join
    """
    import string

    lower_z = 122
    cap_Z   = 90
    rotation = 13
    
    new_sent = []
    for char in sentence: 
        if char in string.ascii_lowercase:
            rot13_char = ord(char) + rotation
            if rot13_char > lower_z:
                rot13_char = ord(char) - rotation
        elif char in string.ascii_uppercase:
            rot13_char = ord(char) + rotation
            if rot13_char > cap_Z:
                rot13_char = ord(char) - rotation
        else:
            rot13_char = ord(char) #if out of spec, keep as is!
        new_sent.append(chr(rot13_char))
    return ''.join(new_sent)
  
sentence = "The quick brown Fox Jumped over The lazy Dog"
print("before:", sentence)
print ("after: ", rot13(sentence), "\n")

sentence = "Gur dhvpx oebja Sbk Whzcrq bire Gur ynml Qbt"
print("before:", sentence)
print ("after: ", rot13(sentence))

"""Output
before: The quick brown Fox Jumped over The lazy Dog
after:  Gur dhvpx oebja Sbk Whzcrq bire Gur ynml Qbt

before: Gur dhvpx oebja Sbk Whzcrq bire Gur ynml Qbt
after:  The quick brown Fox Jumped over The lazy Dog
"""

def num_of_const_vow_words(sentence):
    """
    8.10
    determine the amount of consonants, vowels and words in a string
    """
    vowels = "aioue"
    vowel_count = 0
    consonant_count = 0
    word_count = 0
    words = sentence.split(" ")
    for phrase in words:
        word_count += 1
        for char in phrase:
            if char in vowels:
                vowel_count += 1
            elif char != " ":
                consonant_count += 1
    return (vowel_count, consonant_count, word_count)
sentence = "Once more unto the breach, dear friends, once more"
print ("The sentence: " + "'" + sentence + "'\nhas %d vowels, %d consonants, %d words" 
        % num_of_const_vow_words(sentence))
"""Output
The sentence: 'Once more unto the breach, dear friends, once more'
has 16 vowels, 26 consonants, 9 words
"""

def strip_pound_sig(file):
    """
    9.1
    Stripping away any '#' signs in front
    of the lines in a file
    """
    fo = open(file, "r")
    print("BEFORE:")
    for line in fo:
        print(line.strip("\n"))
    fo.seek(0)
    print ("\nAFTER:")
    for line in fo:
        no_pound_line = line.strip('#')
        print (no_pound_line.strip("\n"))

strip_pound_sig("document.txt")
"""Output
BEFORE:
Once more unto the breach, dear friends, once more;
Or close the wall up with our English dead.
# In peace there's nothing so becomes a man
As modest stillness and humility:
#But when the blast of war blows in our ears,
Then imitate the action of the tiger;
# Stiffen the sinews, summon up the blood,
Disguise fair nature with hard-favour'd rage;

AFTER:
Once more unto the breach, dear friends, once more;
Or close the wall up with our English dead.
 In peace there's nothing so becomes a man
As modest stillness and humility:
But when the blast of war blows in our ears,
Then imitate the action of the tiger;
 Stiffen the sinews, summon up the blood,
Disguise fair nature with hard-favour'd rage;
"""
def display_num_lines(n, f):
    """
    9.2
    display the first "n" lines of "f" file
    """
    fo = open(f, "r")
    for i, txt in enumerate(fo):
        if i <= n:
            print(txt.strip("\n"))         
num = int(input("Please enter an integer: "))
f = input("Please enter your file: ")
display_num_lines((num - 1), f)
"""Output
Please enter an integer: 3
Please enter your file: document.txt
Once more unto the breach, dear friends, once more;
Or close the wall up with our English dead.
# In peace there's nothing so becomes a man
"""

def count_lines_of_file(f):
    """
    9.3
    display number of lines in a document
    """
    fo = open(f, "r")
    num_lines = 0
    for num in fo:
        num_lines += 1
    return num_lines
f = input("Please enter your file: ")
print ("number of lines in file: %d" % count_lines_of_file(f))
"""Output
Please enter your file: document.txt
number of lines in file: 8
"""

"""
10.7
a) The first snippet tries Statement A and sees if it yields an error. If no error, then it proceeds to Statement B. This helps
use determine if Statement A has an error or not.

b) The second snippet tried BOTH statement A and B, and if one yields an error, you will not know which one. If both had errors, then
the except will catch only one, and not tell you which raised the error. This is bad since it doesn't tell us anything useful to fix 
our code.
"""

def demo_trace(fxn):
    """
    problem 12, HW 3
    demo module trace
    Literally tracks and traces a function through a program/script
    """
    import trace
    
    tracer = trace.Trace(count = False, trace = True)
    tracer.run(fxn)
sentence = "H"
fxn = "rot13(sentence)"
demo_trace(fxn)
"""Output
  --- modulename: HW_3, funcname: <module>
<string>(1):  --- modulename: HW_3, funcname: rot13
HW_3.py(65):     import string
HW_3.py(67):     lower_z = 122
HW_3.py(68):     cap_Z   = 90
HW_3.py(69):     rotation = 13
HW_3.py(71):     new_sent = []
HW_3.py(72):     for char in sentence:
HW_3.py(73):         if char in string.ascii_lowercase:
HW_3.py(77):         elif char in string.ascii_uppercase:
HW_3.py(78):             rot13_char = ord(char) + rotation
HW_3.py(79):             if rot13_char > cap_Z:
HW_3.py(83):         new_sent.append(chr(rot13_char))
HW_3.py(72):     for char in sentence:
HW_3.py(84):     return ''.join(new_sent)
 --- modulename: trace, funcname: _unsettrace
trace.py(77):         sys.settrace(None)
"""

def demo_timeit():
    """
    problem 12, HW 3
    demo the module timeit
    module times the performance of a statement/function
    """
    import timeit 
    t = timeit.Timer(lambda: "print (rot13(sentence))")
    print ("Time:", t.timeit(2))
    print ("Repeat:", t.repeat(3))
sentence = "Once more unto the breach, dear friends, once more"
fxn = "print (rot13(sentence))"
demo_timeit()
"""Output
Time: 2.8738345574500055e-06
Repeat: [0.10536955459669838, 0.10393510060473689, 0.10435714373688812]
"""    


