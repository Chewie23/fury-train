import pdb #see problem 11.4
import traceback #see problem 11.5
#--------------------------------------------------------------------------------------
"""
6.14
RPS Game Code
"""
import random
    
def end_state(choice, comp):
    choice_dict = {"r": 1, "p": 2, "s": 3}
    
    difference = comp - choice_dict[choice]
    #below is based on the logic that the difference in choices yields a pattern
    if difference == 0:
        return "Tie"
    elif difference % 3 == 1:
        return "Lose"
    elif difference % 3 == 2:
        return "Win"

def play():
    prompt = "Do you want to play Rock Paper Scissors? Y/N: "
    choice = raw_input(prompt).strip()[0].lower()

    if choice in "yY":
        playing = True
    else:
        playing = False
    return playing

def r_p_s():
    """
    A rousing game of Rock, Paper, Scissors. 
    """
    while True:
        playing = play()
        if playing:
            comp_choice = random.randrange(1, 4)
            prompt = "Please pick [r]ock, [p]aper, or [s]cissors: "
            choice = raw_input(prompt).strip()[0].lower()
            if choice in "rps":
                print end_state(choice, comp_choice)
            else:
                print "Invalid choice. Try again"
        else:
            return "Goodbye"
        
print r_p_s()

"""Output
Do you want to play Rock Paper Scissors? Y/N: y
Please pick [r]ock, [p]aper, or [s]cissors: p
Lose
Do you want to play Rock Paper Scissors? Y/N: y
Please pick [r]ock, [p]aper, or [s]cissors: p
Tie
Do you want to play Rock Paper Scissors? Y/N: y
Please pick [r]ock, [p]aper, or [s]cissors: p
Win
Do you want to play Rock Paper Scissors? Y/N: y
Please pick [r]ock, [p]aper, or [s]cissors: p
Win
Do you want to play Rock Paper Scissors? Y/N: y
Please pick [r]ock, [p]aper, or [s]cissors: p
Lose
Do you want to play Rock Paper Scissors? Y/N: n
Goodbye
"""
#--------------------------------------------------------------------------------------
def hours(minutes):
    """
    11.4
    Convert minutes -> hours + minutes
    """
    MIN_IN_HOUR = 60
    return ("Hours: %r, minutes: %r" % (minutes // MIN_IN_HOUR, minutes % MIN_IN_HOUR))
    
print hours(123)
pdb.set_trace() #for problem 10, making use of pdb and traceback
print hours(384)
"""Output
Hours: 2, minutes: 3
> c:~\hw_4.py(80)<module>()
-> print hours(384)
(Pdb) continue
Hours: 6, minutes: 24
"""
#--------------------------------------------------------------------------------------
def sales_tax(price, sales_tax = .075):
    """
    11.5
    Calculates and adds on sales tax
    """
    return price + (sales_tax * price)
print sales_tax(100)
print sales_tax(100, .085)
try:
    print sales_tax("ab")
except TypeError:
    traceback.print_stack()
    print "--------------------------------------------------"
    traceback.print_exc()
"""Output
107.5
108.5
  File "HW_4.py", line 88, in <module>
    print hours(384)
--------------------------------------------------
Traceback (most recent call last):
  File "HW_4.py", line 88, in <module>
    print hours(384)
  File "HW_4.py", line 100, in sales_tax
    total = price + (sales_tax * price)
TypeError: can't multiply sequence by non-int of type 'float'
"""
#--------------------------------------------------------------------------------------
"""
Code for 11.8
"""
def is_a_leap_year(year):
   """
   5-4
   Finds valid leap year. Must be divisible by 4 AND NOT 100. OR divisible by 400.
   """
   if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
      return year
   return None

def leap_year_list():   
    """
    11.8
    filter() example
    """
    list_o_years = []
    for n in range (1900, 2017):
        list_o_years.append(n)
    return filter(is_a_leap_year, list_o_years)
print leap_year_list()
"""Output
[1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980,
 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
"""

def leap_year_list_2():
    """11.8
    List Comprehension
    """
    leap_year_list = [is_a_leap_year(year) for year in range(1900, 2017) if is_a_leap_year(year) != None]
    return leap_year_list
print leap_year_list_2()
"""Output
[1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980,
 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
 """
 #--------------------------------------------------------------------------------------
def separate_decimals(num_str):
    """
    #Whole sequence makes two lists, 
    one with whole numbers and one with decimals
    """
    num_list = []
    dec_list = num_str.split(".")
    num_list.append(dec_list[0])
    dec_list.remove(dec_list[0])
    dec_list.insert(0, ".")
    return num_list, dec_list
        
 
def dollarize(num): #works. May want to streamline it
    """
    13.3 prelim
    format a number to be "$X,XXX.YY" 
    WITHOUT ".format" or "locale"
    Input: floating point
    """
    is_negative = False
    if num < 0:
        num *= -1
        is_negative = True
    num_str = str(round(num, 2))
    
    if "." in num_str:
        num_list, dec_list = separate_decimals(num_str)
        
    comma = (len("".join(num_list)) // 3) #determines how many commas needed
    num_str = "".join(num_list)
    num_list = list(num_str)
    num_len = len(num_str)
    first_placement = num_len % 3 #determines first comma placement

    if num_len >= 4:
        if first_placement > 0:
            num_list.insert(first_placement, ",")
            for n in range(1, comma):
                num_list.insert(num_len - ((n * 3) - 1), ",")
        else:
            for n in range(1, comma):
                num_list.insert(num_len - (n * 3), ",")
    whole_list = num_list + dec_list
    if is_negative:
        return "-$%s" % "".join(whole_list)
    return "$%s" % "".join(whole_list)
    
print dollarize(1234567.89123)
print dollarize(-1234567.89123)
print dollarize(123.4567)
print dollarize(-1234.567)
"""Output
$1,234,567.89
-$1,234,567.89
$123.46
-$1,234.57
"""