
import whois
import json
import io
import time

#Take the URL file and turn it into an array
f = open('urls.txt')
urls = f.read().splitlines()
print urls

f = open('urlinfo.txt', 'a')

# iterate through the URLs
for url in urls:
	print "Grabbing %s" %url
	whois_data = whois.whois(url)
	f.write(url)

	with io.open('urlinfo.txt', 'a', encoding='utf-8') as f:
		
		f.write(unicode(whois_data))
		
	f = open('urlinfo.txt', 'a')
	f.write("\n \n")
	f.close