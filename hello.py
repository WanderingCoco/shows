#!/usr/bin/env python

#import postgres 

terms = ['california', ', ca', ',ca', 'san francisco', 'oakland']

urls = ["http://www.hiromiuehara.com/en/tour/index.html", "http://www.greyboyallstars.com/tour.php"]

for url in urls: 
	import urllib
	f = urllib.urlopen(url)

	page = f.read()

	pagelower = page.lower()

	found = False

	for term in terms:
		if term in pagelower:
			found = True

	if found:
		print "hooray", url

#fetch http://www.hiromiuehara.com/en/tour/index.html
#scan for 
#- california/
#- CA
#- san francisco
#- oakland
#if found, print

