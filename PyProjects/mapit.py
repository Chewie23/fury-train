import webbrowser
import sys
import pyperclip

#I want open up to directions to a certain location.
#TODO: Getting current location. MAY not be possible, so we just gotta use a variable and grit our teeth.
#Seems like Javascript is the main language to use with Google Maps API

if len(sys.argv) > 1:
    address = ' '.join(sys.arv[1:]) #since "sys.argv" will yield a list of strings
    #for instance: ["mapit.py", "whatever"]. So [1:] simply ignores the "mapit.py"
else:
    address = pyperclip.paste()

#below simply opens up google maps to the address    
#webbrowser.open('https://www.google.com/maps/place/' + address) 

START = '2757 Randers Court, Palo Alto/'
END   = address

webbrowser.open('https://www.google.com/maps/dir/' + START + END)
#Side note, this completely wipes the clipboard, so can't do this ad nauseum
