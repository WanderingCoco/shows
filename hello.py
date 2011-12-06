
terms = ['california', 'ca', 'san francisco', 'oakland']

import urllib
f = urllib.urlopen("http://www.hiromiuehara.com/en/tour/index.html")

page = f.read()

pagelower = page.lower()

found = False

for term in terms:
	if term in pagelower:
		found = True

if found:
	print "hooray"

#fetch http://www.hiromiuehara.com/en/tour/index.html
#scan for 
#- california/
#- CA
#- san francisco
#- oakland
#if found, print