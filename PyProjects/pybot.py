import pyautogui, threading, time

#maybe add the URL in here? Just copy the video ID and have user enter it in the script. Would make it more automated!
#Combine it with the youtube playlist script you made?

def autoplay():
	x_pos       = 187
	y_pos       = 590
	num_seconds = 0
	#clicks and drag the mouse from current position to determined position
	#pyautogui.dragTo(x_pos, y_pos, duration=num_seconds) 

	#moves the mouse (if combined with "dragTo", will still have "clicked" but no longer highlight)
	pyautogui.moveTo(x_pos, y_pos, num_seconds)
	pyautogui.click()
"""
playtime = 240.0

#need a function to run, at an arbitrary time
timer = threading.Timer(playtime,autoplay())
timer.start()

ONLY STARTS TIMER ONCE
"""

playtime = 243 #time for Ryder - Pretty Little Gangster

#This code relies on "time.sleep", and a While loop. Maybe I should make it more graceful? For Loop?
while True:
	autoplay()
	time.sleep(playtime)
	

