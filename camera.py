import time
import cv2
import numpy
import io
import lcd


#vc.set(3,160)
#vc.set(4,120)

def capture(name):
	try:
		lcd.stringlcd(0x80,"frame")
		frame = io.BytesIO()
		time.sleep(1)
		lcd.stringlcd(0x80,"capturing")
		vc = cv2.VideoCapture(0)
		time.sleep(1)
		lcd.stringlcd(0x80,"reading")
		rval, frame = vc.read()
		time.sleep(1)
		lcd.stringlcd(0x80,"saving")
		cv2.imwrite(name,frame)
		time.sleep(1)
		lcd.stringlcd(0x80,"closing")
		time.sleep(1)
		del vc
	except:
		print "Capturing Failed"
		lcd.stringlcd(0x80,"CAPTURING FAILEDD")
		time.sleep(3)
