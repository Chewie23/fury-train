#!/usr/bin/env python
"""
13-20 d. 
__radd__ is the "magic" method of allowing addition of objects as a SECOND argument; 
practically speaking, it allows object that is on the RIGHT side of the "+" operator to be added to a corresponding argument. 
It normally defaults to the LEFT side if using __add__. We do NOT need to use it since as long as 
a class object is on the left side, we can just simply use __add__. But if you HAVE to have a class object 
on the right side of the "+" operator, then __radd__ is needed.

e.  ...Says __repr__() is flawed, since it should always give a valid string expression
    BUT no direction on what to do/no query entered. Will most likely leave this blank

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
time_c = Time60("8:55") #DOES NOT WORK. NEED TO MAKE WORK
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