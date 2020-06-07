import lcd
import RPi.GPIO as GPIO
import sys
import time
import wifi
import datetime
import mcp3202
import webpage

import serial
import thread
import gsm
import os
import camera
import ftp
import thread
from flask import Flask
ser = serial.Serial('/dev/ttyS0',9600)
os.system("sudo service motion start")
lcd.lcd_init()
lcd.stringlcd(0x80,"welcome")

import socket
import fcntl
import struct

def getip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])



#3,5,7,11,13,15
#19,21--spi
#29,31
#12,16,18,22,
#24 -- spi
#26 -- led
#32 -- switch

#outputs

out1 = 3
out2 = 5
out3 = 7
out4 = 11
out5 = 13
out6 = 15

sw  = 32
#inputs

in1 = 12#fire
in2 = 16
in3 = 18
in4 = 22
in5 = 29
in6 = 31

led = 26

GPIO.setup(in1,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(in2,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(in3,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(in4,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(in5,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(in6,GPIO.IN,pull_up_down = GPIO.PUD_UP)

GPIO.setup(out1,GPIO.OUT)
GPIO.output(out1,False)
GPIO.setup(out2,GPIO.OUT)
GPIO.output(out2,False)
GPIO.setup(out3,GPIO.OUT)
GPIO.output(out3,False)
GPIO.setup(out4,GPIO.OUT)
GPIO.output(out4,False)
GPIO.setup(out5,GPIO.OUT)
GPIO.output(out5,True)
GPIO.setup(out6,GPIO.OUT)
GPIO.output(out6,False)


wifi.Connect_wifi()
app = Flask(__name__)

ipaddr = getip('wlan0')
lcd.stringlcd(0x80,"CONNECT TO")
lcd.stringlcd(0xc0,ipaddr)

@app.route("/") 
def hello():
	print 'Hello'
	lcd.stringlcd(0x80,"WELCOME")
	st = "<h1>ROBOT CONTROL</h1><br>"
	st = st + "<br>" + 	\
			  "<a href ='/1'>FRONT</a><br>"  + 	\
			  "<a href ='/2'>BACK</a><br>" +	\
			  "<a href ='/3'>LEFT</a><br>"  + 	\
			  "<a href ='/4'>RIGHT</a><br>" +	\
			  "<a href ='/5'>STOP</a><br>"  + 	\
			  "<br></center></h2>"+"<br><br><iframe width='320' height = '240' src='http://" + ipaddr + ":8081'></iframe> "
	return st
@app.route("/1")
def l1on():
	lcd.stringlcd(0x80,"FRONT")
	GPIO.output(out1,True)
	GPIO.output(out2,False)
	GPIO.output(out3,True)
	GPIO.output(out4,False)
	st = "<h1>ROBOT CONTROL - FRONT</h1><br>"
	st = st + "<h2><center><br>" + 	\
			  "<a href ='/1'>FRONT</a><br>"  + 	\
			  "<a href ='/2'>BACK</a><br>" +	\
			  "<a href ='/3'>LEFT</a><br>"  + 	\
			  "<a href ='/4'>RIGHT</a><br>" +	\
			  "<a href ='/5'>STOP</a><br>"  + 	\
			  "<br></center></h2>"+"<br><br><iframe width='320' height = '240' src='http://" + ipaddr + ":8081'></iframe> "
	return st
@app.route("/2")
def l2on():
	global temperature,hum,ctl
	lcd.stringlcd(0x80,"BACK")
	GPIO.output(out2,True)
	GPIO.output(out1,False)
	GPIO.output(out4,True)
	GPIO.output(out3,False)
	st = "<h1>ROBOT CONTROL - BACK</h1><br>"
	st = st + "<h2><center><br>" + 	\
			  "<a href ='/1'>FRONT</a><br>"  + 	\
			  "<a href ='/2'>BACK</a><br>" +	\
			  "<a href ='/3'>LEFT</a><br>"  + 	\
			  "<a href ='/4'>RIGHT</a><br>" +	\
			  "<a href ='/5'>STOP</a><br>"  + 	\
			  "<br></center></h2>"+"<br><br><iframe width='320' height = '240' src='http://" + ipaddr + ":8081'></iframe> "
	return st
@app.route("/3")
def l3on():
	
	lcd.stringlcd(0x80,"LEFT")
	GPIO.output(out1,True)
	GPIO.output(out2,False)
	GPIO.output(out4,True)
	GPIO.output(out3,False)
	st = "<h1>ROBOT CONTROL - LEFT</h1><br>"
	st = st + "<h2><center><br>" + 	\
			  "<a href ='/1'>FRONT</a><br>"  + 	\
			  "<a href ='/2'>BACK</a><br>" +	\
			  "<a href ='/3'>LEFT</a><br>"  + 	\
			  "<a href ='/4'>RIGHT</a><br>" +	\
			  "<a href ='/5'>STOP</a><br>"  + 	\
			  "<br></center></h2>"+"<br><br><iframe width='320' height = '240' src='http://" + ipaddr + ":8081'></iframe> "
	return st
@app.route("/4")
def l4on():
	
	lcd.stringlcd(0x80,"RIGHT")
	GPIO.output(out2,True)
	GPIO.output(out1,False)
	GPIO.output(out3,True)
	GPIO.output(out4,False)
	st = "<h1>ROBOT CONTROL - RIGHT</h1><br>"
	st = st + "<h2><center><br>" + 	\
			  "<a href ='/1'>FRONT</a><br>"  + 	\
			  "<a href ='/2'>BACK</a><br>" +	\
			  "<a href ='/3'>LEFT</a><br>"  + 	\
			  "<a href ='/4'>RIGHT</a><br>" +	\
			  "<a href ='/5'>STOP</a><br>"  + 	\
			  "<br></center></h2>"+"<br><br><iframe width='320' height = '240' src='http://" + ipaddr + ":8081'></iframe> "
	return st
@app.route("/5")
def l5on():

	lcd.stringlcd(0x80,"STOP")
	GPIO.output(out1,False)
	GPIO.output(out2,False)
	GPIO.output(out3,False)
	GPIO.output(out4,False)
	st = "<h1>ROBOT CONTROL - STOP</h1><br>"
	st = st + "<h2><center><br>" + 	\
			  "<a href ='/1'>FRONT</a><br>"  + 	\
			  "<a href ='/2'>BACK</a><br>" +	\
			  "<a href ='/3'>LEFT</a><br>"  + 	\
			  "<a href ='/4'>RIGHT</a><br>" +	\
			  "<a href ='/5'>STOP</a><br>"  + 	\
			  "<br></center></h2>"+"<br><br><iframe width='320' height = '240' src='http://" + ipaddr + ":8081'></iframe> "
	return st


def httpser(thName,delay):
	app.run(host='0.0.0.0')
	
thread.start_new_thread(httpser,("Thread-1",2,))

while(1):
	
	
	time.sleep(1)
	
	

	print 'Loop'
	



	























