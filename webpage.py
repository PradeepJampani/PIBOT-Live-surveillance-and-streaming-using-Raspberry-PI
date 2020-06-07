import time
import lcd
import urllib2
def browse(ms):
	print ms
	source = "*0#"
	try:
		data = urllib2.urlopen(ms,timeout=30)
		source = data.read()
		print source
	except:
		pass	
	return source
def brw(a,b,c,d,e):
	data = urllib2.urlopen("http://www.gprsserver.in/portlogger.php?a=pir-" + str(a) +"&b=gas-" + str(b) +"&c=fire-"+ str(c) +"&d=temp-"+ str(d) +"&e=ldr-"+ str(e) +"&f=1&g=1&h=1&i=1&j=1&k=c5290&l=logger")
	source = data.read()
	print source
	#return source
