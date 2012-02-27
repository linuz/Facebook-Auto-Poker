#! /usr/bin/python
#############################################################################
# Facebook Auto-Poker Python V1.5											#
# Written By: Dennis Linuz <dennismald@gmail.com>							#
# Auto-pokes anyone on Facebook that has poked you with a Variable Delay    #
# and a file to specify which Facebook IDs NOT to poke (blockPokes.txt)		#
#############################################################################
FACEBOOK_USERNAME = ""
FACEBOOK_PASSWORD = ""
import mechanize, time, os
MAX_DELAY = 60
delay = MAX_DELAY
totalPokes = 0
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open("http://m.facebook.com/pokes")
browser._factory.is_html = True
browser.select_form(nr=0)
browser.form['email'] = FACEBOOK_USERNAME
browser.form['pass'] = FACEBOOK_PASSWORD
browser.submit()
browser._factory.is_html = True
while True:
	try:
		tempPokeCount = 0
		tempPokeNum = 0
		browser.open("http://m.facebook.com/pokes")
		browser._factory.is_html = True
		for l in browser.links(text_regex="Poke back"):
			result = False
			browser._factory.is_html = True
			if os.path.exists("blockPokes.txt"): file = open("blockPokes.txt")
			else: file = " "
			for line in file:
				line = line.replace("\n","")
				if (l.url.find(line) > -1):
					result = True
					tempPokeNum += 1
					break
			if not result:
				browser.follow_link(text_regex="Poke back",nr=tempPokeNum)
				tempPokeCount += 1
				totalPokes += 1
				print "Total Pokes: " + str(totalPokes) + "\n"
		if (tempPokeCount != 0 and delay > 1): delay /= 2
		if (tempPokeCount == 0 and delay < MAX_DELAY): delay *= 2
	except:
		print "There was some sort of error :("
	time.sleep(delay)