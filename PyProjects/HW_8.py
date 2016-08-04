"""
7.  (10) (MT download email) Modify your solution to the previous problem by making your application multithreaded. 
Download email from multiple accounts "simultaneously," sorting by timestamp order. If you only have one email account, have 2 threads downloading odd and even msgs respectively.

8.  (20) 19-5 (GUI Labels, Buttons, Radiobuttons)

10.  (10) (networking) Create a multithreaded version of your solution to Exercise 9a above.

"""
# Problem 5, HW 8: poplib, imaplib, and smtplib modules
"""
poplib:
This module copies over messages from the mail server to the local computer. This primarily is used to download email
To use this, we need to make an object of the class poplib, login and download a message
import poplib
server = poplib.POP3_SSL("pop.<email address server>") #connection to a server
server.user("<username>")
server.pass_("<password>") #login

num_message = len(server.list()[1])

for n in range(num_message): #downloads a message and prints it out
    for i in server.retr(n + 1) [1]:
        if n.startswith("Subject"):
            print "\t" + i
            break

server.quit()
            
imaplib:
Module that allows client to communicate with IMAP4 servers via sent commands. Can download, send, delete email from mail server.
Much like poplib, we need to make an object of the imaplib class for the server, login and password.

import imaplib
mail = iaplib.IMAP4_SSL("imap.gmail.com")
mail.login("user@gmail.com", "user_password")
mail.list() # gets a list of folders in gmail
mail.select("inbox") #we connected to inbox. From there, we can send commands and do what we will
result, data = mail.search(None, "ALL")
 
ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1] # get the latest
 
result, data = mail.fetch(latest_email_id, "(RFC822)")
 
raw_email = data[0][1] #this fetches the latest email

smtplib:
This module connects to a mail server and sends an email message. This is primarily used to send email.
The steps to smtplib are similar if not outright identical. Create an object, login, and do whatever action 
(in this case, send an email)

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = ("From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message. ")
mail = smtplib.SMTP('local_host')
mail.sendmail(sender, receivers, message)
"""

#----------------------------------------------------------------------------------------------------------------------
# Probelm 6, HW 8: Download email
import poplib
import StringIO, rfc822
import string, random

def download_latest_mail(server_address, user, password):
    server = poplib.POP3_SSL(server_address) #connection to a server
    server.user(user)
    server.pass_(password) #login

    resp, items, octets = server.list()

    # download latest message
    id, size = string.split(items[len(items) - 1])
    resp, text, octets = server.retr(id)

    text = string.join(text, "\n")
    file = StringIO.StringIO(text)

    message = rfc822.Message(file)

    return (message, message.items())
    
user = "testingforpythoncs21b"
password = raw_input("Enter your password: ")
server_address = "pop.mail.yahoo.com"

message, message_list = download_latest_mail(server_address, user, password)

for k, v in message_list:
    print k, "=", v

print message.fp.read()

"""Output
Enter your password: ************
received = by 98.138.105.254; Thu, 10 Mar 2016 17:34:32 +0000
received-spf = pass (domain of yahoo.com designates 98.138.229.35 as permitted sender)
from = <testingforpythoncs21b@yahoo.com>
authentication-results = mta1502.mail.ne1.yahoo.com  from=yahoo.com; domainkeys=neutral (no sig);  from=yahoo.com; dkim=pass (ok)
content-type = multipart/alternative;
 boundary="----=_Part_335132_814269383.1457631272100"
x-ymailisg = 
...
...
mime-version = 1.0
to = "testingforpythoncs21b@yahoo.com" <testingforpythoncs21b@yahoo.com>
references = <923999792.335133.1457631272103.JavaMail.yahoo.ref@mail.yahoo.com>
x-yahoo-newman-id = 754808.3499.bm@omp1036.mail.ne1.yahoo.com
dkim-signature = v=1; a=rsa-sha256; c=relaxed/relaxed; d=yahoo.com; s=s2048; t=1457631438; bh=rc7b44iXxfKDMWuEnz83QyA9C/ioFuPhJY3u3+KbEoc=; h=Date:From:Reply-To:To:Subject:References:From:Subject; b=ooTzvw41YuYM3dcIAPVKCRPoO8Q7zXyGW4y513R9ZrfOkBa7UL8axr4Pfz5NFHEs6O+0SU04duWvPJOBsEHU+j7CZhlbwnxP8daFHbr8R+3O7qqxOFw7cRqfWTDxGIeXI5uz7tHZU58+ubwA4X3TkL+C6A3bD4z44pPtwZYmjlhvaEiTwJ7BQ7iGu/j1vc99N2BVOV6pi4Zk8VLYQs4qeayutBgtSfrG0hEbxbdWTzUzVT9TG+9+kd7Jorch7V1rD9pZ+iHNV4rGFqobSe111ryC+AC8SGtqy0Pb0dv9jzbf092cFh9KIpzp6o2P19jbzNVhGBCcZLUt382RosgHQQ==
date = Thu, 10 Mar 2016 17:34:32 +0000 (UTC)
x-ymail-osg = ...
...
...
message-id = <923999792.335133.1457631272103.JavaMail.yahoo@mail.yahoo.com>
x-apparently-to = testingforpythoncs21b@yahoo.com; Thu, 10 Mar 2016 17:37:21 +0000
reply-to = <testingforpythoncs21b@yahoo.com>
x-originating-ip = [98.138.229.35]
subject = Mark Twain
------=_Part_335132_814269383.1457631272100
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

Never argue with a fool; onlookers may not be able to tell the difference. =
=E2=80=94Mark Twain
------=_Part_335132_814269383.1457631272100
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

<html><head></head><body><div style=3D"color:#000; background-color:#fff; f=
ont-family:HelveticaNeue, Helvetica Neue, Helvetica, Arial, Lucida Grande, =
sans-serif;font-size:16px"><div dir=3D"ltr" id=3D"yui_3_16_0_1_145763087285=
3_5137">Never argue with a fool; onlookers may not be able to tell the diff=
erence. =E2=80=94<em>Mark Twain</em></div></div></body></html>
------=_Part_335132_814269383.1457631272100--

"""
#----------------------------------------------------------------------------------------------------------------------
# Problem 7, HW 8: Multi-thread version of Problem 6




#----------------------------------------------------------------------------------------------------------------------
# 19-5: GUI, Buttons, Radiobuttons




#----------------------------------------------------------------------------------------------------------------------
# 20-2 a-c: urllib
import urllib

def download_website(URL):
    website = urllib.urlopen(URL) #20-2 a. urllib.urlopen()
    return website.read()
    
def retrieve_website(URL):
    website = urllib.urlretrieve(URL) #20-2 b. urllib.urlretrieve()
    return website
#//////////////////////////////////////////////////////////////////
#20-2 a. urllib.urlopen
URL = "http://python.org/"        
python_website = download_website(URL)
print python_website

print "################################################################################\n"

URL = "http://google.com"        
google_website = download_website(URL)
print google_website
#Output presented last, due to sheer amount of html text

#//////////////////////////////////////////////////////////////////
#20-2 b. urllib.retrieve

URL = "http://python.org/"

python_website = retrieve_website(URL)

print python_website

URL = "http://google.com/"

google_website = retrieve_website(URL)
print google_website

"""Output 20-2 b.
('/tmp/tmpeq62wx', <httplib.HTTPMessage instance at 0xffd631cc>)
('/tmp/tmpd1fCBt', <httplib.HTTPMessage instance at 0xffd6308c>)
"""

"""Output 20-2 c.
These two differ from socket by:
1) WAY shorter code
2) No need to check if connected/explicitly ask for a connection or send commands
3) It is, as the above answer states, more abstracted from the network, and all the heavy lifting happens behind the scenes

I personally prefer urllib2, not urllib. But urllib is better than socket because it abstracts the process to something more simple and easier to digest.
"""

#----------------------------------------------------------------------------------------------------------------------
# Problem 10, HW 8. Multithreading answer for 20-2 a.
import threading










#Output 20-2 a. Warning. It is really long.
"""
<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

    <meta name="application-name" content="Python.org">
    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">
    <meta name="apple-mobile-web-app-title" content="Python.org">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="HandheldFriendly" content="True">
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="cleartype" content="on">
    <meta http-equiv="imagetoolbar" content="false">

    <script src="/static/js/libs/modernizr.js"></script>

    <link href="/static/stylesheets/style.css" rel="stylesheet" type="text/css" title="default" />
    <link href="/static/stylesheets/mq.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty" />


    <!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.css" rel="stylesheet" type="text/css" media="screen" />


    <![endif]-->


    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">
    <link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">


    <meta name="msapplication-TileImage" content="/static/metro-icon-144x144-precomposed.png"><!-- white shape -->
    <meta name="msapplication-TileColor" content="#3673a5"><!-- python blue -->
    <meta name="msapplication-navbutton-color" content="#3673a5">

    <title>Welcome to Python.org</title>

    <meta name="description" content="The official home of the Python Programming Language">
    <meta name="keywords" content="Python programming language object oriented web free open source software license documentation download community">


    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Python.org">
    <meta property="og:title" content="Welcome to Python.org">
    <meta property="og:description" content="The official home of the Python Programming Language">

    <meta property="og:image" content="https://www.python.org/static/opengraph-icon-200x200.png">
    <meta property="og:image:secure_url" content="https://www.python.org/static/opengraph-icon-200x200.png">

    <meta property="og:url" content="https://www.python.org/">

    <link rel="author" href="/static/humans.txt">




    <script type="application/ld+json">
     {
       "@context": "http://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>


    <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>

</head>

<body class="python home" id="homepage">

    <div id="touchnav-wrapper">

        <div id="nojs" class="do-not-print">
            <p><strong>Notice:</strong> While Javascript is not essential for this website, your interaction with the content will be limited. Please turn Javascript on for the full experience. </p>
        </div>

        <!--[if lt IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p><strong>Notice:</strong> Your browser is <em>ancient</em> and <a href="http://www.ie6countdown.com/">Microsoft agrees</a>. <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience a better web.</p>
        </div>
        <![endif]-->

        <!-- Sister Site Links -->
        <div id="top" class="top-bar do-not-print">

            <nav class="meta-navigation container" role="navigation">


                <div class="skip-link screen-reader-text">
                    <a href="#content" title="Skip to content">Skip to content</a>
                </div>


                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-down"><span>&#9660;</span></span> Close
                </a>



<ul class="menu" role="tree">

    <li class="python-meta current_item selectedcurrent_branch selected">
        <a href="/" title="The Python Programming Language" class="current_item selectedcurrent_branch selected">Python</a>
    </li>

    <li class="psf-meta ">
        <a href="/psf-landing/" title="The Python Software Foundation" >PSF</a>
    </li>

    <li class="docs-meta ">
        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>
    </li>

    <li class="pypi-meta ">
        <a href="https://pypi.python.org/" title="Python Package Index" >PyPI</a>
    </li>

    <li class="jobs-meta ">
        <a href="/jobs/" title="Python Job Board" >Jobs</a>
    </li>

    <li class="shop-meta ">
        <a href="/community/" title="Python Community" >Community</a>
    </li>

</ul>


                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> The Python Network
                </a>

            </nav>

        </div>

        <!-- Header elements -->
        <header class="main-header" role="banner">
            <div class="container">

                <h1 class="site-headline">
                    <a href="/"><img class="python-logo" src="/static/img/python-logo.png" alt="python&trade;"></a>
                </h1>

                <div class="options-bar do-not-print">


                    <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">&equiv;</span> Menu</a><form class="search-the-site" action="/search/" method="get">
                        <fieldset title="Search Python.org">

                            <span aria-hidden="true" class="icon-search"></span>

                            <label class="screen-reader-text" for="id-search-field">Search This Site</label>
                            <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">

                            <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
                                GO
                            </button>


                            <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->

                        </fieldset>
                    </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">
                        <ul class="navigation menu" aria-label="Adjust Text Size on Page">
                            <li class="tier-1 last" aria-haspopup="true">
                                <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>
                                    <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><div class="winkwink-nudgenudge">
                        <ul class="navigation menu" aria-label="Social Media Navigation">
                            <li class="tier-1 last" aria-haspopup="true">
                                <a href="#" class="action-trigger">Socialize</a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a href="http://plus.google.com/+Python"><span aria-hidden="true" class="icon-google-plus"></span>Google+</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a href="http://www.facebook.com/pythonlang?fref=ts"><span aria-hidden="true" class="icon-facebook"></span>Facebook</a></li>
                                    <li class="tier-2 element-3" role="treeitem"><a href="http://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>
                                    <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><div class="account-signin">
                        <ul class="navigation menu" aria-label="Social Media Navigation">
                            <li class="tier-1 last" aria-haspopup="true">

                                <a href="/accounts/login/" title="Sign Up or Sign In to Python.org">Sign In</a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a href="/accounts/signup/">Sign Up / Register</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a href="/accounts/login/">Sign In</a></li>
                                </ul>

                            </li>
                        </ul>
                    </div>

                </div><!-- end options-bar -->

                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">


<ul class="navigation menu" role="menubar" aria-label="Main Navigation">



    <li id="about" class="tier-1 element-1  " aria-haspopup="true">
        <a href="/about/" title="" class="">About</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>

</ul>


    </li>



    <li id="downloads" class="tier-1 element-2  " aria-haspopup="true">
        <a href="/downloads/" title="" class="">Downloads</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>

</ul>


    </li>



    <li id="documentation" class="tier-1 element-3  " aria-haspopup="true">
        <a href="/doc/" title="" class="">Documentation</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="https://docs.python.org/devguide/" title="">Developer&#39;s Guide</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>

</ul>


    </li>



    <li id="community" class="tier-1 element-4  " aria-haspopup="true">
        <a href="/community/" title="" class="">Community</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>

        <li class="tier-2 element-9" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>

</ul>


    </li>



    <li id="success-stories" class="tier-1 element-5  " aria-haspopup="true">
        <a href="/about/success/" title="success-stories" class="">Success Stories</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/success/#arts" title="">Arts</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/success/#business" title="">Business</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/success/#education" title="">Education</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/success/#engineering" title="">Engineering</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/about/success/#government" title="">Government</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="/about/success/#scientific" title="">Scientific</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/about/success/#software-development" title="">Software Development</a></li>

</ul>


    </li>



    <li id="news" class="tier-1 element-6  " aria-haspopup="true">
        <a href="/blogs/" title="News from around the Python world" class="">News</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>

</ul>


    </li>



    <li id="events" class="tier-1 element-7  " aria-haspopup="true">
        <a href="/events/" title="" class="">Events</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events/" title="">Python Events</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>

</ul>


    </li>





</ul>


                </nav>

                <div class="header-banner "> <!-- for optional "do-not-print" class -->

        <div id="dive-into-python" class="flex-slideshow slideshow">

            <ul class="launch-shell menu" id="launch-shell">
                <li>
                    <a class="button prompt" id="start-shell" data-shell-container="#dive-into-python" href="/shell/">&gt;_
                        <span class="message">Launch Interactive Shell</span>
                    </a>
                </li>
            </ul>

            <ul class="slides menu">

                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Fibonacci series up to n</span>
>>> def fib(n):
>>>     a, b = 0, 1
>>>     while a &lt; n:
>>>         print(a, end=' ')
>>>         a, b = b, a+b
>>>     print()
>>> fib(1000)
<span class="output">0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987</span></code></pre></div>
                    <div class="slide-copy"><h1>Functions Defined</h1>
<p>The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">More about defining functions in Python&nbsp;3</a></p></div>
                </li>

                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: List comprehensions</span>
>>> fruits = ['Banana', 'Apple', 'Lime']
>>> loud_fruits = [fruit.upper() for fruit in fruits]
>>> print(loud_fruits)
<span class="output">['BANANA', 'APPLE', 'LIME']</span>

<span class="comment"># List and the enumerate function</span>
>>> list(enumerate(fruits))
<span class="output">[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]</span></code></pre></div>
                    <div class="slide-copy"><h1>Compound Data Types</h1>
<p>Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. <a href="//docs.python.org/3/tutorial/introduction.html#lists">More about lists in Python&nbsp;3</a></p></div>
                </li>

                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple arithmetic</span>
>>> 1 / 2
<span class="output">0.5</span>
>>> 2 ** 3
<span class="output">8</span>
>>> 17 / 3  <span class="comment"># classic division returns a float</span>
<span class="output">5.666666666666667</span>
>>> 17 // 3  <span class="comment"># floor division</span>
<span class="output">5</span></code></pre></div>
                    <div class="slide-copy"><h1>Intuitive Interpretation</h1>
<p>Calculations are simple with Python, and expression syntax is straightforward: the operators <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code> work as expected; parentheses <code>()</code> can be used for grouping. <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">More about simple math functions in Python&nbsp;3</a>.</p></div>
                </li>

                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple output (with Unicode)</span>
>>> print("Hello, I'm Python!")
<span class="output">Hello, I'm Python!</span>

<span class="comment"># Input, assignment</span>
>>> name = input('What is your name?\n')
>>> print('Hi, %s.' % name)
<span class="output">What is your name?
Python
Hi, Python.</span></code></pre></div>
                    <div class="slide-copy"><h1>Quick &amp; Easy to Learn</h1>
<p>Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. <a href="//docs.python.org/3/tutorial/">Whet your appetite</a> with our Python&nbsp;3 overview.</p>
                   </div>
                </li>

                <li>
                    <div class="slide-code"><pre><code><span class=\"comment\"># For loop on a list</span>
>>> numbers = [2, 4, 6, 8]
>>> product = 1
>>> for number in numbers:
...    product = product * number
...
>>> print('The product is:', product)
<span class=\"output\">The product is: 384</span></code></pre></div>
                    <div class="slide-copy"><h1>All the Flow You&rsquo;d Expect</h1>
<p>Python knows the usual control flow statements that other languages speak &mdash; <code>if</code>, <code>for</code>, <code>while</code> and <code>range</code> &mdash; with some of its own twists, of course. <a href="//docs.python.org/3/tutorial/controlflow.html">More control flow tools in Python&nbsp;3</a></p></div>
                </li>

            </ul>
        </div>


                </div>


        <div class="introduction">
            <p>Python is a programming language that lets you work quickly <span class="breaker"></span>and integrate systems more effectively. <a class="readmore" href="/doc/">Learn More</a></p>
        </div>


             </div><!-- end .container -->
        </header>

        <div id="content" class="content-wrapper">
            <!-- Main Content Column -->
            <div class="container">

                <section class="main-content " role="main">






                <div class="row">

                    <div class="small-widget get-started-widget">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Get Started</h2>
<p>Whether you're new to programming or an experienced developer, it's easy to learn and use Python.</p>
<p><a href="/about/gettingstarted/">Start with our Beginner&rsquo;s Guide</a></p>
                    </div>

                    <div class="small-widget download-widget">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-download"></span>Download</h2>
<p>Python source code and installers are available for download for all versions! Not sure which version to use? <a href="https://wiki.python.org/moin/Python2orPython3">Check here</a>.</p>
<p>Latest: <a href="/downloads/release/python-351/">Python 3.5.1</a> - <a href="/downloads/release/python-2711/">Python 2.7.11</a></p>
                    </div>

                    <div class="small-widget documentation-widget">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>
<p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>
<p><a href="https://docs.python.org">docs.python.org</a></p>
                    </div>

                    <div class="small-widget jobs-widget last">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-jobs"></span>Jobs</h2>
<p>Looking for work or have a Python related position that you're trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.</p>
<p><a href="//jobs.python.org">jobs.python.org</a></p>
                    </div>

                </div>

                <div class="list-widgets row">

                    <div class="medium-widget blog-widget">

                        <div class="shrubbery">

                            <h2 class="widget-title"><span aria-hidden="true" class="icon-news"></span>Latest News</h2>
                            <p class="give-me-more"><a href="http://blog.python.org" title="More News">More</a></p>

                            <ul class="menu">


                                <li>
<time datetime="2015-12-07T05:51:00+00:00"><span class="say-no-more">2015-</span>12-07</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/F9ApGB7BGB4/python-351-and-python-344rc1-are-now.html">Python 3.5.1 and Python 3.4.4rc1 are now available for download. ...</a></li>

                                <li>
<time datetime="2015-12-05T22:14:00.000005+00:00"><span class="say-no-more">2015-</span>12-05</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/X8l2dWcjfLs/python-2711-released.html">The latest bugfix release of the Python 2.7 series is ...</a></li>

                                <li>
<time datetime="2015-11-22T02:43:00.000006+00:00"><span class="say-no-more">2015-</span>11-22</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/_sGRwFhJK4s/python-2711-release-candidate-1.html">The first release candidate of Python 2.7.11, the next release ...</a></li>

                                <li>
<time datetime="2015-09-13T14:28:00.000006+00:00"><span class="say-no-more">2015-</span>09-13</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/a6zwstMbRrg/python-350-has-been-released.html">Python 3.5.0 is now&nbsp;available for download. Python 3.5.0 is the ...</a></li>

                                <li>
<time datetime="2015-09-09T13:43:00.000002+00:00"><span class="say-no-more">2015-</span>09-09</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/D-XkdrMEtE0/python-350-release-candidate-4-released.html">Python 3.5.0rc4 is now&nbsp;available for download. This is a last-minute ...</a></li>

                            </ul>
                        </div><!-- end .shrubbery -->

                    </div>

                    <div class="medium-widget event-widget last">

                        <div class="shrubbery">

                            <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
                            <p class="give-me-more"><a href="/events/calendars/" title="More Events">More</a></p>

                            <ul class="menu">



                                <li>
<time datetime="2016-03-12T00:00:00+00:00"><span class="say-no-more">2016-</span>03-12</time>
 <a href="/events/python-events/400/">PyData Amsterdam 2016</a></li>



                                <li>
<time datetime="2016-03-19T04:30:00+00:00"><span class="say-no-more">2016-</span>03-19</time>
 <a href="/events/python-user-group/407/">BangPypers - Bangalore Python Users Group</a></li>



                                <li>
<time datetime="2016-04-01T00:00:00+00:00"><span class="say-no-more">2016-</span>04-01</time>
 <a href="/events/python-events/390/">PyDay Loja 2016</a></li>



                                <li>
<time datetime="2016-04-02T00:00:00+00:00"><span class="say-no-more">2016-</span>04-02</time>
 <a href="/events/python-user-group/408/">Django Girls Ica</a></li>



                                <li>
<time datetime="2016-04-02T00:00:00+00:00"><span class="say-no-more">2016-</span>04-02</time>
 <a href="/events/python-events/369/">PythonCamp Cologne 2016</a></li>


                            </ul>
                        </div>

                    </div>

                </div>

                <div class="row">

                    <div class="medium-widget success-stories-widget">


                        <div class="shrubbery">


                            <h2 class="widget-title"><span aria-hidden="true" class="icon-success-stories"></span>Success Stories</h2>
                            <p class="give-me-more"><a href="/success-stories/" title="More Success Stories">More</a></p>


                            <div class="success-story-item" data-weight="0" id="success-story-2" style="display: none;">

                            <blockquote>
                                <a href="/success-stories/industrial-light-magic-runs-python/">ILM runs a batch processing environment capable of modeling, rendering and compositing tens of thousands of motion picture frames per day. Thousands of machines running Linux, IRIX, Compaq Tru64, OS X, Solaris, and Windows join together to provide a production pipeline used by ~800 users daily. Speed of development is key, and Python was a faster way to code (and re-code) the programs that control this production pipeline.</a>
                            </blockquote>

                            <table cellpadding="0" cellspacing="0" border="0" width="100%" class="quote-from">
                                <tbody>
                                    <tr>

                                        <td><p><a href="/success-stories/industrial-light-magic-runs-python/">Industrial Light &amp; Magic Runs on Python</a> <em>by Tim Fortenberry</em></p></td>
                                    </tr>
                                </tbody>
                            </table>
                            </div>


                        </div><!-- end .shrubbery -->

                    </div>

                    <div class="medium-widget applications-widget last">
                        <div class="shrubbery">
                            <h2 class="widget-title"><span aria-hidden="true" class="icon-python"></span>Use Python for&hellip;</h2>
<p class="give-me-more"><a href="/about/apps" title="More Applications">More</a></p>

<ul class="menu">
    <li><b>Web Programming</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.djangoproject.com/">Django</a>, <a class="tag" href="http://www.pylonsproject.org/">Pyramid</a>, <a class="tag" href="http://bottlepy.org">Bottle</a>, <a class="tag" href="http://tornadoweb.org">Tornado</a>, <a href="http://flask.pocoo.org/" class="tag">Flask</a>, <a class="tag" href="http://www.web2py.com/">web2py</a></span></li>
    <li><b>GUI Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.wxpython.org/">wxPython</a>, <a class="tag" href="http://wiki.python.org/moin/TkInter">tkInter</a>, <a class="tag" href="http://www.pygtk.org">PyGtk</a>, <a class="tag" href="https://wiki.gnome.org/Projects/PyGObject">PyGObject</a>, <a class="tag" href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt</a></span></li>
    <li><b>Scientific and Numeric</b>:
        <span class="tag-wrapper">
<a class="tag" href="http://www.scipy.org">SciPy</a>, <a class="tag" href="http://pandas.pydata.org/">Pandas</a>, <a href="http://ipython.org" class="tag">IPython</a></span></li>
    <li><b>Software Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://buildbot.net/">Buildbot</a>, <a class="tag" href="http://trac.edgewall.org/">Trac</a>, <a class="tag" href="http://roundup.sourceforge.net/">Roundup</a></span></li>
    <li><b>System Administration</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.ansible.com">Ansible</a>, <a class="tag" href="http://www.saltstack.com">Salt</a>, <a class="tag" href="https://www.openstack.org">OpenStack</a></span></li>
</ul>

                        </div><!-- end .shrubbery -->
                    </div>

                </div>


                <div class="pep-widget">

                    <h2 class="widget-title">
                        <span class="prompt">&gt;&gt;&gt;</span> <a href="/dev/peps/">Python Enhancement Proposals<span class="say-no-more"> (PEPs)</span></a>: The future of Python<span class="say-no-more"> is discussed here.</span>
                        <a aria-hidden="true" class="rss-link" href="/dev/peps/peps.rss"><span class="icon-feed"></span> RSS</a>
                    </h2>




                </div>

                                <div class="psf-widget">

                    <div class="python-logo"></div>

                    <h2 class="widget-title">
    <span class="prompt">&gt;&gt;&gt;</span> <a href="/psf/">Python Software Foundation</a>
</h2>
<p>The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. <a class="readmore" href="/psf/">Learn more</a> </p>
<p class="click-these">
    <a class="button" href="/users/membership/">Become a Member</a>
    <a class="button" href="/psf/donations/">Donate to the PSF</a>
</p>
                </div>




                </section>








            </div><!-- end .container -->
        </div><!-- end #content .content-wrapper -->

        <!-- Footer and social media list -->
        <footer id="site-map" class="main-footer" role="contentinfo">
            <div class="main-footer-links">
                <div class="container">


                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>



<ul class="sitemap navigation menu do-not-print" role="tree" id="container">

    <li class="tier-1 element-1">
        <a href="/about/" >About</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>

</ul>


    </li>

    <li class="tier-1 element-2">
        <a href="/downloads/" >Downloads</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>

</ul>


    </li>

    <li class="tier-1 element-3">
        <a href="/doc/" >Documentation</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="https://docs.python.org/devguide/" title="">Developer&#39;s Guide</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>

</ul>


    </li>

    <li class="tier-1 element-4">
        <a href="/community/" >Community</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>

        <li class="tier-2 element-9" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>

</ul>


    </li>

    <li class="tier-1 element-5">
        <a href="/about/success/" title="success-stories">Success Stories</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/success/#arts" title="">Arts</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/success/#business" title="">Business</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/success/#education" title="">Education</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/success/#engineering" title="">Engineering</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/about/success/#government" title="">Government</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="/about/success/#scientific" title="">Scientific</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/about/success/#software-development" title="">Software Development</a></li>

</ul>


    </li>

    <li class="tier-1 element-6">
        <a href="/blogs/" title="News from around the Python world">News</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>

</ul>


    </li>

    <li class="tier-1 element-7">
        <a href="/events/" >Events</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events/" title="">Python Events</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>

</ul>


    </li>

    <li class="tier-1 element-8">
        <a href="/dev/" >Contributing</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="http://docs.python.org/devguide/" title="">Developer&#39;s Guide</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="http://bugs.python.org/" title="">Issue Tracker</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="http://pythonmentors.com/" title="">Core Mentorship</a></li>

</ul>


    </li>

</ul>


                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>


                </div><!-- end .container -->
            </div> <!-- end .main-footer-links -->

            <div class="site-base">
                <div class="container">

                    <ul class="footer-links navigation menu do-not-print" role="tree">
                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>
                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>
                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>
                        <!--<li class="tier-1 element-3"><a href="#"><span class="say-no-more">Website</span> Colophon</a></li>-->
                    </ul>

                    <div class="copyright">
                        <p><small>
                            <span class="pre">Copyright &copy;2001-2016.</span>
                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                            &nbsp;<span class="pre"><a href="/privacy/">Privacy Policy</a></span>
                        </small></p>
                    </div>

                </div><!-- end .container -->
            </div><!-- end .site-base -->

        </footer>

    </div><!-- end #touchnav-wrapper -->


    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')</script>

    <script src="/static/js/libs/masonry.pkgd.min.js"></script>

    <script type="text/javascript" src="/static/js/main-min.js" charset="utf-8"></script>


    <!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.js" charset="utf-8"></script>


    <![endif]-->

    <!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.js" charset="utf-8"></script>


    <![endif]-->






</body>
</html>

################################################################################

<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. 
Google has many special features to help you find exactly what you're looking for." name="description"><meta content="noodp" name="robots"><meta content="text/html; charset=UTF-8" 
http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script>(function(){window.google=
{kEI:'dzXjVtf6CsvojwOMzI6wDA',kEXPI:'201663,3700274,3700388,4029815,4031109,4032678,4033307,4036509,4036527,4038012,4039268,4041303,4042552,4042784,4042792,4043492,4045841,4046304,4048347,
4049549,4049557,4051159,4051241,4052304,4054284,4054551,4054853,4055202,4056038,4057134,4057169,4057316,4057836,4058099,4058117,4058298,4058330,4058337,4058384,4059318,4059374,4059513,4059767,
4060014,4060329,4060886,4061089,4061155,4061381,4061483,4061564,4061670,4061738,4061782,4061887,4061925,4061935,4062333,4062672,8300095,8300272,8300310,8502946,8502985,8503012,8503132,8503303,
8503306,8503367,8503404,8503605,8503853,8503925,8503927,10200083',authuser:0,kscs:'c9c918f0_24'};google.kHL='en';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&
(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b}
;google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.wl=function(a,b){try{google.ml(Error(a),!1,b)}catch(d){}};google.time=function(){return(new Date).
getTime()};google.log=function(a,b,d,e,g){a=google.logUrl(a,b,d,e,g);if(""!=a){b=new Image;var c=google.lc,f=google.li;c[f]=b;b.onerror=b.onload=b.onabort=function(){delete c[f]};window.google&&window.google.
vel&&window.google.vel.lu&&window.google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,d,e,g){var c="",f=google.ls||"";if(!d&&-1==b.search("&ei=")){var h=google.getEI(e),c="&ei="+h;-1==b.search
("&lei=")&&((e=google.getLEI(e))?c+="&lei="+e:h!=google.kEI&&(c+="&lei="+google.kEI))}a=d||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+c+f+"&zx="+google.time();/^http:/i.test(a)&&google.https()&&(google.ml
(Error("a"),!1,{src:a,glmm:1}),a="");return a};google.y={};google.x=function(a,b){google.y[a.id]=[a,b];return!1};google.load=function(a,b,d){google.x({id:a+k++},function(){google.load(a,b,d)})};var k=0;})();
var _gjwl=location;function _gjuc(){var a=_gjwl.href.indexOf("#");if(0<=a&&(a=_gjwl.href.substring(a),0<a.indexOf("&q=")||0<=a.indexOf("#q="))&&(a=a.substring(1),-1==a.indexOf("#"))){for(var d=0;d<a.length;)
{var b=d;"&"==a.charAt(b)&&++b;var c=a.indexOf("&",b);-1==c&&(c=a.length);b=a.substring(b,c);if(0==b.indexOf("fp="))
a=a.substring(0,d)+a.substring(c,a.length),c=d;else if("cad=h"==b)return 0;d=c}_gjwl.href="/search?"+a+"&cad=h";return 1}return 0}
function _gjh(){!_gjuc()&&window.google&&google.x&&google.x({id:"GJH"},function(){google.nav&&google.nav.gjh&&google.nav.gjh()})};
window._gjh&&_gjh();</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}
.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}
.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}
</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:
scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:
normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}a.gb1,a.gb2,
a.gb3,a.gb4{color:#11c !important}body{background:#fff;color:black}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}
a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff !important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc 
#999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;
outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script></script><link href="/images/branding/product/ico/googleg_lodp.ico" rel="shortcut icon"></head>
<body bgcolor="#fff"><script>(function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}
if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}
}
})();</script><div id="mngb">    <div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="http://www.google.com/imghp?hl=en&tab=wi">Images</a> <a class=gb1 href="http://maps.google.com/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> 
<a class=gb1 href="http://www.youtube.com/?tab=w1">YouTube</a> <a class=gb1 href="http://news.google.com/nwshp?hl=en&tab=wn">News</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> 
<a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 style="text-decoration:none" href="https://www.google.com/intl/en/options/"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%>
<nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.com/history/optout?hl=en" class=gb4>Web History</a> | <a  href="/preferences?hl=en" class=gb4>Settings</a> | 
<a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://www.google.com/" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div>    </div><center><span id="prt" style="display:block"> <div><style>.pmoabs{background-color:#fff;border:1px solid #E5E5E5;color:#666;font-size:13px;padding-bottom:20px;position:absolute;right:2px;top:3px;z-index:986}#pmolnk{border-radius:2px;-moz-border-radius:2px;-webkit-border-radius:2px}.kd-button-submit{border:1px solid #3079ed;background-color:#4d90fe;background-image:-webkit-gradient(linear,left top,left bottom,from(#4d90fe),to(#4787ed));background-image:-webkit-linear-gradient(top,#4d90fe,#4787ed);background-image:-moz-linear-gradient(top,#4d90fe,#4787ed);background-image:-ms-linear-gradient(top,#4d90fe,#4787ed);background-image:-o-linear-gradient(top,#4d90fe,#4787ed);background-image:linear-gradient(top,#4d90fe,#4787ed);filter:progid:DXImageTransform.Microsoft.gradient(startColorStr='#4d90fe',EndColorStr='#4787ed')}.kd-button-submit:hover{border:1px solid #2f5bb7;background-color:#357ae8;background-image:-webkit-gradient(linear,left top,left bottom,from(#4d90fe),to(#357ae8));background-image:-webkit-linear-gradient(top,#4d90fe,#357ae8);background-image:-moz-linear-gradient(top,#4d90fe,#357ae8);background-image:-ms-linear-gradient(top,#4d90fe,#357ae8);background-image:-o-linear-gradient(top,#4d90fe,#357ae8);background-image:linear-gradient(top,#4d90fe,#357ae8);filter:progid:DXImageTransform.Microsoft.gradient(startColorStr='#4d90fe',EndColorStr='#357ae8')}.kd-button-submit:active{-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,0.3);-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.3);box-shadow:inset 0 1px 2px rgba(0,0,0,0.3)}#pmolnk a{color:#fff;display:inline-block;font-weight:bold;padding:5px 20px;text-decoration:none;white-space:nowrap}.xbtn{color:#999;cursor:pointer;font-size:23px;line-height:5px;padding-top:5px}.padi{padding:0 8px 0 10px}.padt{padding:5px 20px 0 0;color:#444}.pads{text-align:left;max-width:200px}</style> <div class="pmoabs" id="pmocntr2" style="behavior:url(#default#userdata);display:none"> <table border="0"> <tr> <td colspan="2"> <div class="xbtn" onclick="google.promos&&google.promos.toast&& google.promos.toast.cpc()" style="float:right">&times;</div> </td> </tr> <tr> <td class="padi" rowspan="2"> <img src="/images/icons/product/chrome-48.png"> </td> <td class="pads">A better way to browse the web</td> </tr> <tr> <td class="padt"> <div class="kd-button-submit" id="pmolnk"> <a href="/chrome/browser/?hl=en&amp;brand=CHNG&amp;utm_source=en-hpp&amp;utm_medium=hpp&amp;utm_campaign=en" onclick="google.promos&&google.promos.toast&& google.promos.toast.cl()">Get Google Chrome</a> </div> </td> </tr> </table> </div> <script type="text/javascript">(function(){var a={v:{}};a.v.mb=50;a.v.kb=10;a.v.La="body";a.v.Mb=!0;a.v.Pb=function(b,c){var d=a.v.Cb();a.v.Eb(d,b,c);a.v.Qb(d);a.v.Mb&&a.v.Nb(d)};a.v.Qb=function(b){(b=a.v.Na(b))&&0<b.forms.length&&b.forms[0].submit()};a.v.Cb=function(){var b=document.createElement("iframe");b.height=0;b.width=0;b.style.overflow="hidden";b.style.top=b.style.left="-100px";b.style.position="absolute";document.body.appendChild(b);return b};a.v.Na=function(b){return b.contentDocument||b.contentWindow.document};a.v.Eb=function(b,c,d){b=a.v.Na(b);b.open();d=["<",a.v.La,'><form method=POST action="',d,'">'];for(var e in c)c.hasOwnProperty(e)&&d.push('<textarea name="',e,'">',c[e],"</textarea>");d.push("</form></",a.v.La,">");b.write(d.join(""));b.close()};a.v.Pa=function(b,c){c>a.v.kb?google&&google.ml&&google.ml(Error("ogcdr"),!1,{cause:"timeout"}):b.contentWindow?a.v.Ob(b):window.setTimeout(function(){a.v.Pa(b,c+1)},a.v.mb)};a.v.Ob=function(b){document.body.removeChild(b)};a.v.Nb=function(b){a.v.Ab(b,"load",function(){a.v.Pa(b,0)})};a.v.Ab=function(b,c,d){b.addEventListener?b.addEventListener(c,d,!1):b.attachEvent&&b.attachEvent("on"+c,d)};var m={Ub:0,$:1,ka:2,va:5,Tb:6};a.s={};a.s.ya={Ya:"i",ta:"d",$a:"l"};a.s.U={Aa:"0",ma:"1"};a.s.Ba={wa:1,ta:2,ra:3};a.s.S={Sa:"a",Wa:"g",W:"c",ub:"u",tb:"t",Aa:"p",lb:"pid",Ua:"eid",vb:"at"};a.s.Za=window.location.protocol+"//www.google.com/_/og/promos/";a.s.Va="g";a.s.wb="z";a.s.Fa=function(b,c,d,e){var f=null;switch(c){case m.$:f=window.gbar.up.gpd(b,d,!0);break;case m.va:f=window.gbar.up.gcc(e)}return null==f?0:parseInt(f,10)};a.s.Ib=function(b,c,d){return c==m.$?null!=window.gbar.up.gpd(b,d,!0):!1};a.s.Ca=function(b,c,d,e,f,h,k,l){var g={};g[a.s.S.Aa]=b;g[a.s.S.Wa]=c;g[a.s.S.Sa]=d;g[a.s.S.vb]=e;g[a.s.S.Ua]=f;g[a.s.S.lb]=1;k&&(g[a.s.S.W]=k);l&&(g[a.s.S.ub]=l);if(h)g[a.s.S.tb]=h;else return google.ml(Error("knu"),!1,{cause:"Token is not found"}),null;return g};a.s.Ia=function(b,c,d){if(b){var e=c?a.s.Va:a.s.wb;c&&d&&(e+="?authuser="+d);a.v.Pb(b,a.s.Za+e)}};a.s.Db=function(b,c,d,e,f,h,k){b=a.s.Ca(c,b,a.s.ya.ta,a.s.Ba.ta,d,f,null,e);a.s.Ia(b,h,k)};a.s.Gb=function(b,c,d,e,f,h,k){b=a.s.Ca(c,b,a.s.ya.Ya,a.s.Ba.wa,d,f,e,null);a.s.Ia(b,h,k)};a.s.Lb=function(b,c,d,e,f,h,k,l,g,n){switch(c){case m.va:window.gbar.up.dpc(e,f);break;case m.$:window.gbar.up.spd(b,d,1,!0);break;case m.ka:g=g||!1,l=l||"",h=h||0,k=k||a.s.U.ma,n=n||0,a.s.Db(e,h,k,f,l,g,n)}};a.s.Jb=function(b,c,d,e,f){return c==m.$?0<d&&a.s.Fa(b,c,e,f)>=d:!1};a.s.Fb=function(b,c,d,e,f,h,k,l,g,n){switch(c){case m.va:window.gbar.up.iic(e,f);break;case m.$:c=a.s.Fa(b,c,d,e)+1;window.gbar.up.spd(b,d,c.toString(),!0);break;case m.ka:g=g||!1,l=l||"",h=h||0,k=k||a.s.U.Aa,n=n||0,a.s.Gb(e,h,k,1,l,g,n)}};a.s.Kb=function(b,c,d,e,f,h){b=a.s.Ca(c,b,a.s.ya.$a,a.s.Ba.ra,d,e,null,null);a.s.Ia(b,f,h)};var p={Rb:"a",Vb:"l",Sb:"c",Ta:"d",ra:"h",wa:"i",lc:"n",ma:"x",dc:"ma",jc:"mc",kc:"mi",Wb:"pa",Xb:"pc",Zb:"pi",ac:"pn",$b:"px",Yb:"pd",mc:"gpa",qc:"gpi",sc:"gpn",tc:"gpx",nc:"gpd"};a.o={};a.o.R={ab:"hplogo",rb:"pmocntr2"};a.o.U={qb:"0",ma:"1",Ra:"2"};a.o.w=document.getElementById(a.o.R.rb);a.o.Xa=16;a.o.nb=2;a.o.pb=20;google.promos=google.promos||{};google.promos.toast=google.promos.toast||{};a.o.qa=function(b){a.o.w&&(a.o.w.style.display=b?"":"none",a.o.w.parentNode&&(a.o.w.parentNode.style.position=b?"relative":""))};a.o.Qa=function(b){try{if(a.o.w&&b&&b.es&&b.es.m){var c=window.gbar.rtl(document.body)?"left":"right";a.o.w.style[c]=b.es.m-a.o.Xa+a.o.nb+"px";a.o.w.style.top=a.o.pb+"px"}}catch(d){google.ml(d,!1,{cause:a.o.T+"_PT"})}};google.promos.toast.cl=function(){try{a.o.Da==m.ka&&a.s.Kb(a.o.Ga,a.o.V,a.o.U.Ra,a.o.Ka,a.o.Ha,a.o.Ja),window.gbar.up.sl(a.o.V,a.o.T,p.ra,a.o.Ea(),1)}catch(b){google.ml(b,!1,{cause:a.o.T+"_CL"})}};google.promos.toast.cpc=function(){try{a.o.w&&(a.o.qa(!1),a.s.Lb(a.o.w,a.o.Da,a.o.R.Ma,a.o.Ga,a.o.Bb,a.o.V,a.o.U.ma,a.o.Ka,a.o.Ha,a.o.Ja),window.gbar.up.sl(a.o.V,a.o.T,p.Ta,a.o.Ea(),1))}catch(b){google.ml(b,!1,{cause:a.o.T+"_CPC"})}};a.o.Oa=function(){try{if(a.o.w){var b=276,c=document.getElementById(a.o.R.ab);c&&(b=Math.max(b,c.offsetWidth));var d=parseInt(a.o.w.style.right,10)||0;a.o.w.style.visibility=2*(a.o.w.offsetWidth+d)+b>document.body.clientWidth?"hidden":""}}catch(e){google.ml(e,!1,{cause:a.o.T+"_HOSW"})}};a.o.yb=function(){var b=["gpd","spd","aeh","sl"];if(!window.gbar||!window.gbar.up)return!1;for(var c=0,d;d=b[c];c++)if(!(d in window.gbar.up))return!1;return!0};a.o.Hb=function(){return a.o.w.currentStyle&&"absolute"!=a.o.w.currentStyle.position};google.promos.toast.init=function(b,c,d,e,f,h,k,l,g,n,q,r){try{if(!a.o.yb())google.ml(Error("apa"),!1,{cause:a.o.T+"_INIT"});else if(a.o.w)if(e==m.ka&&!l==!g)google.ml(Error("tku"),!1,{cause:"zwieback: "+g+", gaia: "+l}),a.o.qa(!1);else if(a.o.R.W="toast_count_"+c+(q?"_"+q:""),a.o.R.Ma="toast_dp_"+c+(r?"_"+r:""),a.o.T=d,a.o.V=b,a.o.Da=e,a.o.Ga=c,a.o.Bb=f,a.o.Ka=l?l:g,a.o.Ha=!!l,a.o.Ja=k,a.s.Ib(a.o.w,e,a.o.R.Ma,c)||a.s.Jb(a.o.w,e,h,a.o.R.W,c)||a.o.Hb())a.o.qa(!1);else{a.s.Fb(a.o.w,e,a.o.R.W,c,f,a.o.V,a.o.U.qb,a.o.Ka,a.o.Ha,a.o.Ja);if(!n){try{window.gbar.up.aeh(window,"resize",a.o.Oa)}catch(t){}window.lol=a.o.Oa;window.gbar.elr&&a.o.Qa(window.gbar.elr());window.gbar.elc&&window.gbar.elc(a.o.Qa);a.o.qa(!0)}window.gbar.up.sl(a.o.V,a.o.T,p.wa,a.o.Ea())}}catch(t){google.ml(t,!1,{cause:a.o.T+"_INIT"})}};a.o.Ea=function(){var b=a.s.Fa(a.o.w,a.o.Da,a.o.R.W,a.o.Ga);return"ic="+b};})();</script> <script type="text/javascript">(function(){var sourceWebappPromoID=144002;var sourceWebappGroupID=5;var payloadType=5;var cookieMaxAgeSec=2592000;var dismissalType=5;var impressionCap=25;var gaiaXsrfToken='';var zwbkXsrfToken='';var kansasDismissalEnabled=false;var sessionIndex=0;var invisible=false;window.gbar&&gbar.up&&gbar.up.r&&gbar.up.r(payloadType,function(show){if (show){google.promos.toast.init(sourceWebappPromoID,sourceWebappGroupID,payloadType,dismissalType,cookieMaxAgeSec,impressionCap,sessionIndex,gaiaXsrfToken,zwbkXsrfToken,invisible,'0612');}
});})();</script> </div> </span><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" 
id="hplogo" onload="window.lol&&lol()"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" 
value="ISO-8859-1" type="hidden"><input value="en" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;
margin:4px 0"><input style="color:#000;margin:0;padding:5px 8px 0 6px;vertical-align:top" autocomplete="off" class="lst" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0">
<span class="ds"><span class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" value="I'm Feeling Lucky" name="btnI" 
onclick="if(this.form.q.value)this.checked=1; else top.location='/doodles/'" type="submit"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=en&amp;authuser=0">
Advanced search</a><a href="/language_tools?hl=en&amp;authuser=0">Language tools</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"></form><div id="gac_scont"></div><div style="font-size:83%;min-height:
3.5em"><br></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/en/ads/">Advertising▒Programs</a><a href="/services/">Business Solutions</a>
<a href="https://plus.google.com/116899029375914044550" rel="publisher">+Google</a><a href="/intl/en/about.html">About Google</a></div></div><p style="color:#767676;font-size:8pt">&copy; 2016 - 
<a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script>(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.
innerHeight;if(!a||!b)var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body,a=d.clientWidth,b=d.clientHeight;a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw
="+a+"&bih="+b+"&ei="+google.kEI);})();})();</script><div id="xjsd"></div><div id="xjsi"><script>(function(){function c(b){window.setTimeout(function(){var a=document.createElement("script");a.src=b;document.getElementById
("xjsd").appendChild(a)},0)}google.dljp=function(b,a){google.xjsu=b;c(a)};google.dlj=c;})();(function(){window.google.xjsrm=[];})();if(google.y)google.y.first=[];if(!google.xjs){window._=window._||{};window._._DumpException=
function(e){throw e};if(google.timers&&google.timers.load.t){google.timers.load.t.xjsls=new Date().getTime();}google.dljp('/xjs/_/js/k\x3dxjs.hp.en_US.Oi4DpV96uiI.O/m\x3dsb_he,d/rt\x3dj/d\x3d1/t\x3dzcms/rs\x3dACT90oHAXLT3Pr
5eedTte6Acz7wdnJEYXQ','/xjs/_/js/k\x3dxjs.hp.en_US.Oi4DpV96uiI.O/m\x3dsb_he,d/rt\x3dj/d\x3d1/t\x3dzcms/rs\x3dACT90oHAXLT3Pr5eedTte6Acz7wdnJEYXQ');google.xjs=1;}google.pmc={"sb_he":{"agen":true,"cgen":true,"client":"heirloom-hp"
,"dh":true,"dhqt":true,"ds":"","fl":true,"host":"google.com","isbh":28,"jam":0,"jsonp":true,"msgs":{"cibl":"Clear Search","dym":"Did you mean:","lcky":"I\u0026#39;m Feeling Lucky","lml":"Learn more","oskt":"Input tools",
"psrc":"This search was removed from your \u003Ca href=\"/history\"\u003EWeb History\u003C/a\u003E","psrl":"Remove","sbit":"Search by image","srch":"Google Search"},"ovr":{},"pq":"","refpd":true,"rfs":[],"scd":10,"sce":5,
"stok":"vyPZcegovUnFOKxl3eT4AdA8aq8"},"d":{}};google.y.first.push(function(){if(google.med){google.med('init');google.initHistory();google.med('history');}});if(google.j&&google.j.en&&google.j.xi){window.setTimeout
(google.j.xi,0);}
</script></div></body></html>

"""


#----------------------------------------------------------------------------------------------------------------------
# Problem 10, HW 8: Networking



