import urllib2
import time
refreshcnt=0
url=raw_input("Enter the site to check");
x=raw_input("Enter the time duration to refresh");
x=int(x);
url="http://"+url
response = urllib2.urlopen(url)
html = response.read()
htmlnew=html
while html==htmlnew:
	time.sleep(x)
	try:
		htmlnew=urllib2.urlopen(url).read()
	except IOError:
		print "Can't open site"
		break
	refreshcnt+=1
	print "Refresh Count",refreshcnt
	for i in xrange(min(len(htmlnew),len(html))):
		if htmlnew[i] != html[i]:
			print(htmlnew[i-20:i+20])
			print(html[i-20:i+20])
			break
print("The site has updated!");
	
