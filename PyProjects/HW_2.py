def bullcrap(a): #GOTTA FINISH THIS BULL CRAP. BECAUSE IT'S SOME BULL CRAP.BULLCRAP.
   """
   7-5 a, b
   SOME BULL CRAP. gotta have the book. Need page 270 - 271
   """
   pass

def is_a_leap_year(year):
   """
   5-4
   Finds valid leap year. Must be divisible by 4 AND NOT 100. OR divisible by 400.
   """
   if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
      return True
   return False
	
year = 1992
if is_a_leap_year(year):
   print (year, "is a leap year!")
else:
   print (year, "is NOT a leap year!")

def give_back_change(amount):
   """
   5-5
   Find coin increments to add up to number of amount
   Assuming amount is in integers and under 100
   """
   change = []
   for coin in [25, 10, 5, 1]:
      num = amount // coin
      print (num)
      change.append(num)
      print (change)
      amount -= (coin * num)

   return tuple(change)

amount = 80
print ("%d quarters, %d dimes, %d nickels and %d pennies" % give_back_change(amount))


def add_sales_tax(price):
   """
   5-7
   Calculates and adds on sales tax
   """
   sales_tax = .075 * price
   total = price + sales_tax
   return total
  
price = 1.75
print ("Total is: %.2f" % add_sales_tax(price))


def convert_to_minutes(hours, minutes):
   """
   5-13 (hrs & mins)
   converts hours and minutes to total minutes
   """
   hours_in_min = hours * 60
   total_min = hours_in_min + minutes
   return total_min

hours = 3
minutes = 23
print ("Total time in minutes: %d" % convert_to_minutes(hours, minutes))



def sorting_largest_to_smallest_num(n_list):
   """
   6-3a
   sorts largest to smallest number in a list
   """
   a = len(n_list)
   for i in range(a):
      for n in range(a - 1):
         if n_list[n] < n_list[i]:
            n_list[n], n_list[i] = n_list[i], n_list[n]
   return n_list
n_list = [4, 1, 5, 3, 2, 6]
print(n_list)
sorting_largest_to_smallest_num(n_list)
print (n_list)

def sorting_largest_to_smallest_alpha(a_list):
   """
   6-3b
   sorts largest to smallest letter in a list
   """
   a = len(a_list)
   for i in range(a):
      for n in range(a - 1):
         if a_list[n] < a_list[i]:
            a_list[i], a_list[n] = a_list[n], a_list[i]
   return a_list
a_list = ["a", "c", "b", "e", "d"]
print(a_list)
sorting_largest_to_smallest_alpha(a_list)
print (a_list)

def reverse_str(str):
   """
   6-5a
   display string one char at a time, but in reverse.
   """
   new_string = []
   for n in range(len(str)):
      new_string.append(str[len(str) - n - 1])
   return ''.join(new_string)
str = "WHAT UP"
print(str)
print(reverse_str(str))

def two_strings_match(str1, str2):
   """
   6-5b
   compare two strings WITHOUT cmp(), and see if two strings match
   """
   if len(str1) != len(str2):
      return False
   else:
      for n in range(len(str1)):
         if str1[n] != str2[n]:
            return False
      return True
str1 = "Hello"
str2 = "Hello"
if two_strings_match (str1, str2):
   print ("The strings %r and %r match!" % (str1, str2))
else:
   print ("The strings %r and %r DO NOT match!" % (str1, str2))

      
def is_palindrome(str):
   """
   6-5c
   see if string is a palindrome, or reads same forward and reverse
   """
   str1 = str
   str2 = reverse_str(str)
   return two_strings_match(str1, str2)
str = "101"
print(str)
if is_palindrome(str):
   print ("%r is a palindrome" % str)
else:
   print ("%r is NOT a palindrome" % str)

def make_palindrome(str):
   """
   6-5d
   Append reverse string onto forward string and make a Frakenstein monster of a string, 
   that make it into an illedgible palindrome
   Against God's wishes
   May He have mercy on your soul
   """
   str1 = str
   str2 = reverse_str(str)
   palind = str1 + str2
   return palind
str = "abcd"
print (str)
print (make_palindrome(str))

def invert_capital(str):
   """
   6-10
   inverts capital letters to lower case and vica versa
   Ex. string = "Hello THar"
   after function: hELLO thAR"
   """
   new_string = []
   for n in range(len(str)):
      if str[n].isupper():
         new_string.append(str[n].lower())
      else:
         new_string.append(str[n].upper())
   return ''.join(new_string)
str = "AAAbbbbCCCCC"
print(str)
print (invert_capital(str))

def home_made_range(begin, ending, increment):
   """
   8-2
   users give 3 numbers, determining the parameters of the range (beginning, end)
   and the increment to get from one end to the other
   inclusive.
   EX. beginning = 2, end = 26, increment = 4
   2, 6, 10, 14, 18, 22, 26. INCLUSVIE!
   """
   cool_list = []
   try:
      if int(ending) % int(increment) == 0:
         for i in range(int(begin), (int(ending) + int(increment)), int(increment)):
            cool_list.append(i)
      else: 
         for i in range(int(begin), int(ending), int(increment)):
            cool_list.append(i)
   except ValueError:
      print ("That is not an integer!")
      exit (0)
   return cool_list
begin = input("Please enter an integer to begin with: ")
ending = input("Please enter an integer to end at: ")
increment = input("Please enter an integer to increment from beginning to end: ")

print(home_made_range(begin, ending, increment))
   


