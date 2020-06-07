#import gsm
import lcd
import RPi.GPIO as GPIO
import thread
import sys
import time
import serial
import mcp3202
import gsm
import datetime
import wifi
import webpage

gps_location = ""
ser = serial.Serial('/dev/ttyAMA0',9600)

lcd.lcd_init()
lcd.stringlcd(0x80,"welcome")

hb = 3



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(hb,GPIO.IN,pull_up_down = GPIO.PUD_UP)

lcd.stringlcd(0x80,"WELCOME")
wifi.Connect_wifi()
gsm.Gsminit()

def hbcal():
	count = 0
	op=0
	ex=0
	while(1):
		ex = ex+1
		if(ex>5):
			return 40000
		op = 0;
		count = 0
		while(GPIO.input(hb) == 0):
			op = op + 1
			time.sleep(0.0001)
			if(op >= 5000):
				op = 0
				break
			count = count + 1
		while(GPIO.input(hb) == 1):
			op = op +1
			time.sleep(0.001)
			if(op >= 5000):
				break
			count = count + 1
		break
	return count
cnt=0
total = 0

number = ""
try:
	while 1:
		x = gsm.ser.read()
		if(x == '*'):
			number = gsm.ser.read(10)
			print numberlcd.stringlcd(0x80,number)
			time.sleep(5)
			break
except:
	pass
premin = 0
pmin = 0	
hbval = 0
while(1):
	
	temperature = mcp3202.read(0,0) + 11
	lcd.stringlcd(0x80,"HB:"+str(hbval))
	lcd.stringlcd(0xc0, "Temp:"+str(temperature)+"F")
	
	while(1):
		hbval = 5000 - hbcal()
		hbval = hbval / 44
		print hbval
		if(hbval == 0):
			cnt=0
			total = 0
			break
		total = total + hbval
		cnt = cnt + 1
		if(cnt == 20):
			cnt=0
			hbval = total / 20
			total = 0
			break
	if(hbval == 0):
		print 'No HB'
		lcd.stringlcd(0x80,"No HB")
		lcd.stringlcd(0xc0, "Temp:"+str(temperature)+"F")
	else:
		if(hbval > 110 ):
			lcd.stringlcd(0x80,"Sensor Problm")
			lcd.stringlcd(0xc0, "Temp:"+str(temperature)+"F")
		elif(hbval < 60 ):
			lcd.stringlcd(0x80,"Sensor Problm")
			lcd.stringlcd(0xc0, "Temp:"+str(temperature)+"F")
		else:
			lcd.stringlcd(0x80,"HB:"+str(hbval))
			lcd.stringlcd(0xc0, "Temp:"+str(temperature)+"F")
			if(hbval > 78):
				lcd.stringlcd(0x80,"SMS Sending")
				gsm.Sendmsg(number,"High Heart Beat:" + str(hbval)+" Temperature : " + str(temperature))
				time.sleep(7)
				lcd.stringlcd(0x80,"Calling")
				gsm.ser.write('ATD'+number+';\r\n')
				time.sleep(10)
	if(temperature > 103):
		lcd.stringlcd(0x80,"SMS Sending")
		gsm.Sendmsg(number,"High Temperature : " + str(temperature) + "Heart Beat:" + str(hbval))
		time.sleep(7)
		lcd.stringlcd(0x80,"Calling")
		gsm.ser.write('ATD'+number+';\r\n')
		time.sleep(10)
	a = datetime.datetime.now()
	pastmin = pmin
	pmin = a.minute
	if(pmin != pastmin):
		print 'min spent sending data to server'
		lcd.stringlcd(0x80,"sending to server")
		webpage.brw(hbval,temperature)
		lcd.stringlcd(0x80,"sent to server")
		time.sleep(1)
	n=0
	while(1):
		n = n+1
		if(n == 10):
			break
		try:
			x = gsm.ser.read()
			if(x == 'R'):
				x = gsm.ser.read()
				if(x == 'I'):
					lcd.stringlcd(0x80,"Ring received")
					lcd.stringlcd(0x80,"SMS Sending")
					gsm.Sendmsg(number,"Temperature : " + str(temperature) + " Heart Beat:" + str(hbval))
					time.sleep(4)
					lcd.stringlcd(0x80,"SMS Sent")
		except:
			pass
	#time.sleep(1)

