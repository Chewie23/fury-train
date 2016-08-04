"""
Goal: Scrape Euler problems into a database

Selenium + PhantomJS on Windows is kind of slow.

TODO:
- Make a working protoype of getting ONE problem. Then extrapolate from there.
    - Read table of links
    - Get links' text for title
    - Access links
    - Scrape corresponding page's text, put in sql database
    - Go back to main link page //This right here? This is the main problem. Selenium doesn't have a graceful way of accessing link and going back
- Read database

Ideas to solve above problem:
    1) 
    - Store the links in a list or file
    - Loop through the entire list/file and click the links each iteration
    - Go back to main page to click stored link (see: http://stackoverflow.com/questions/27626783/python-selenium-browser-driver-back)
    - Also see: http://stackoverflow.com/questions/24775988/how-to-navigate-to-a-new-webpage-in-selenium
    2)
    - Scrape each link, store it into a list
    - Loop through list, and have the driver.get(new_URL) each iteration
    - And also scrape the words each iteration as well.
    - This seems to be the less elegant way/just uses the basics of driver.get() really

Some useful info:
(td class="id_column") contains the column number and underneath is the link to the problem

"""
import sqlite3 #need to actually use this. Probably learn it too. Don't worry about overengineering. Make something, then make it bette/simpler.
#Course logically speaking, all I need is a text file to store all this
from selenium import webdriver

path = r"C:\Users\achu\Desktop\Misc\Phantomjs\bin\phantomjs.exe"
web_page = "https://projecteuler.net/archives"
problem_1 = "https://projecteuler.net/problem=1"


#should this driver variable be global or in a function?
driver = webdriver.PhantomJS(executable_path = path) #seems like this is the only way to get PhantomJS on Windows.

#driver.get(problem_1)

def save_prompt(driver, URL):
    driver.get(URL)
    print (driver.find_element_by_class_name("problem_content").text) #works in getting prompt for problem. 


#save_prompt(driver, problem_1)#currently just prints it out

#How do we "enter" the link, grab the stuff and go back to main page?

"""
#driver.find_element_by_xpath("//a[contains(@href, 'problem')]").click() #works in clicking the link. Now what? 
Doesn't seem to be an elegant way of clicking the link, doing something, and going back
The easiest solution is the bluntest: store all links in advance (in a list), "driver.get(URL_link)" and do stuff in a loop
"""

"""
#NOTE. YOU NEED TO DO element**s** to find all the elements. Not a singular element (Under docs for Locating Elements)
for element in driver.find_elements_by_xpath("//a[contains(@href, 'problem')]"): #This is the href tag text
    print (element.text) #prints problems' titles from page 1
#Crap. I guess I have to know XPATH. I stole this from http://stackoverflow.com/questions/33887410/python-selenium-locate-elements-by-href
""" 

driver.get(web_page)

links =[]

for element in driver.find_elements_by_xpath("//a[contains(@href, 'problem')]"): #This is searching the href tag text
    links.append(element.get_attribute('href')) #gets link URL (problems 1-50)
    #to get the problem title, do "print(element.text)"

for URL in links:
    with open('Euler.txt', 'ab') as f: #need to open this as a binary file to write in binary text
    #Need to append to have file contain all prompts
        driver.get(URL)
        f.write(driver.find_element_by_class_name("problem_content").text.encode('ascii', 'ignore')) #doesn't like the encoding and need to convert back to a string
        f.write('\n\n'.encode('ascii', 'ignore'))

driver.close()