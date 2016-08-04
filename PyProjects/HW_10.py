"""
I: (100%) HW 10 (coding):
 

1.  (100) (users & passwords VI) Create a web application of your users and passwords application. At a minimum, it should have the following screens and be publicly accessible.

 

    [5] Documentation: Python docstrings for classes, modules, methods, functions. Use a tool like pydoc or Epydoc or Sphinx to create single PDF or HTML doc of all the documentation for your application.

    [5] Unit tests: each tests a functional unit of your app, i.e., username verify (does username already exist), user validation (valid username+passwd combo), add user, remove user, admin check, etc.

    [10] Login screen, including a "register new user" link in case of new users.

    [20] Registration screen

        Prompt for username and password (not plain text)

        If username taken, show red text to user and prompt for another username

        Checkbox for admins—if box is checked, new user will have admin privileges.

            NOTE 1: create a default administrator with username "admin", passwd "istrator21b"

            NOTE 2: only admins can create admins

    [30] Main screen (should be a "logout" link at top of each page)

        Come up with a service worthy of having users wanting to sign-up for your service. Examples:

            Manage stock portfolio (i.e., Yahoo! Finance) w/on-demand stock price fetching

            Global cities weather dashboard (i.e., Open Weather Map) w/specified dates

            Restaurant reservations (i.e., [unofficial] Open Table [API]) w/real bookings

            Social posts dashboard (i.e., Facebook, Twitter, Instagram, Google+)

    [30] Admin screen (same functions as in HW, i.e., add, delete, list users; perhaps more if desired)

 

Choose a Python web framework, i.e., Django, Pyramid, Google App Engine, etc. Choose where you host your app: 
Google App Engine (cloud.google.com/appengine) has a free quota, and some places that offer free Python web hosting: codecondo.com/5-platforms-provide-free-django-app-hosting

You may wish to use a powerful 3rd-party tool to make API requests: docs.python-requests.org

 

It may seem like a lot of work for just 10 points for this class, but an app like this can be put on resumes, 
in a GitHub repo for feedback, and its source code should be taken to job interviews!

 

You have several weeks to implement this solution: recommend you create a command-line version first, 
then as you learn web programming and frameworks, to migrate your app. As before, try to keep your code modular, 
so with skill (not luck), you can use the same Python source code for both apps.
"""