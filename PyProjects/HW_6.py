"""
Problems:

7.  (20) 13-4 (users & passwords IV) I hate this "add bullcrap to more bullcrap" problem. Why. Whyyyy

"""
#----------------------------------------------------------------------------------------------------------------------------
#Problem 5, HW 6
def is_a_leap_year(year):
   """
   Finds valid leap year. Must be divisible by 4 AND NOT 100. OR divisible by 400.
   """
   if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
      return year
   return None

def genex_leap_year():
    return (is_a_leap_year(year) for year in range(1900, 2017) if is_a_leap_year(year) != None)

for n in genex_leap_year():
    print n
"""Output
1904
1908
1912
1916
1920
1924
1928
1932
1936
1940
1944
1948
1952
1956
1960
1964
1968
1972
1976
1980
1984
1988
1992
1996
2000
2004
2008
2012
2016
"""
#----------------------------------------------------------------------------------------------------------------------------
#Problem 6a, HW 6. And difference between generator fxn vs generator exp
import operator
def pass_tuple_in(tup, *fxn):
    """
    pass in a tuple to multiple functions
    """
    for func in fxn:
        yield func(*tup)

for n in pass_tuple_in((1, 2), operator.add, operator.mul, operator.sub):
    print n
"""Output
3
2
-1
"""

"""
6b. HW 6 
Both generator functions and expressions are iterators and creates a value on the go, but the main differences are:

Generators are functions that 'yield' the results one at a time and require multiple lines. 
Which means it can have more complex logic and have more info (potentially).

Generator expressions are one line statements that return an iterator, much like line comprehensions (similar format also). 
Which makes it more compact and have simpler logic.
"""
    
#----------------------------------------------------------------------------------------------------------------------------
#Problem 13-3 a-c. And why dollarize can't be used verbatim 
class MoneyFmt(object):
    def __init__(self, value = 0.0):
        self.value = float(value)
    
    def update(self, value = None):
        """
        Method that checks if value is updated with valid value
        """
        try:
            self.value = float(value)
        except ValueError:
            pass
            
    def __nonzero__(self):
        """
        Checks if value is nonzero
        """
        if self.value != 0:
            return True
        return False
    
    def __repr__(self):
        """
        returns a string that is a printable representation of the object
        """
        return repr(self.value)
    
    def __str__(self):
    """
    Magic Method that allows object to be printed
    Making use of str.format
    """
        if self.value < 0:
            self.value *= -1
            return '-${:,.2f}'.format(self.value)
        return'${:,.2f}'.format(self.value)

cash = MoneyFmt("123")
print cash
cash.update(-155)
print cash
print cash.__nonzero__()
cash.update(1234567.89)
print cash
"""Output
$123.00
-$155.00
True
$1,234,567.89
"""
"""
Cannot use dollarize() by itself because you can't "print" dollarize after it formats the number.
It is essentially trying to "print" a function that doesn't return anything.
You COULD do "print MoneyFmt.dollarize()" but that is more convoluted than just using the __str__() method
You need to use the __str__ in order to make it printable
Otherwise, you would have to use I/O in the class/method in order to display the result,
which is the bane of all Python/Programming.
"""
#----------------------------------------------------------------------------------------------------------------------------
# Problem 13-9, FIFO
class FIFO(object):
    def __init__(self, que):
        self.que = que
    
    def enqueue(self, val):
        """
        loads value into back of the queue
        """
        try:
            self.que.append(val)
        except AttributeError:
            return "Invalid queue value, error code 0"
    
    def dequeue(self):
        """
        returns front value and deletes it from the list
        """
        try:
            return self.que.pop(0)
        except (AttributeError, IndexError):
            return "Invalid queue value, error code 1"

que = [1, 2, 3, 4]
print "unmodified list: ", que
fifa = FIFO(que)
fifa.enqueue(14)
print "enqueued list: ", que
print "dequeued value: ", fifa.dequeue()
print "dequeued list: ", que
"""Output
unmodified list:  [1, 2, 3, 4]
enqueued list:  [1, 2, 3, 4, 14]
dequeued value:  1
dequeued list:  [2, 3, 4, 14]
"""
#----------------------------------------------------------------------------------------------------------------------------
#Problem 13-10 FIFO + stack combo class
class FICombo(object):
    def __init__(self, que_list):
        self.que_list = que_list
    
    def shift(self):
    """
    returns front value and deletes it from the list
    """
        try:
            return self.que_list.pop(0)
        except (AttributeError, IndexError):
            return "Invalid queue value, error code 0"
    
    def unshift(self, val):
    """
    adds value to front of list
    """
        try:
            self.que_list.insert(0, val)
        except AttributeError:
            return "Invalid queue value, error code 1"
            
    def push(self, val):
    """
    adds value to back of list
    """
        self.que_list.append(val)
    
    def pop_out(self):
    """
    returns back value and deletes it from the list
    """
        try:
            return self.que_list.pop()
        except (AttributeError, IndexError):
            return "Invalid queue value, error code 2"

que_list = [1, 2, 3, 4, 5 ,6, 7]
fic = FICombo(que_list)
print "unmodified list: ", que_list
print "shifted value: ", fic.shift()
print "shifted list: ", que_list
fic.unshift(15)
print "unshifted list: ", que_list
fic.push(23)
print "pushed list: ", que_list
print "popped value: ", fic.pop_out()
print "popped list", que_list
            
"""Output
unmodified list:  [1, 2, 3, 4, 5, 6, 7]
shifted value:  1
shifted list:  [2, 3, 4, 5, 6, 7]
unshifted list:  [15, 2, 3, 4, 5, 6, 7]
pushed list:  [15, 2, 3, 4, 5, 6, 7, 23]
popped value:  23
popped list [15, 2, 3, 4, 5, 6, 7]
"""