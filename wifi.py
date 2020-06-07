import os
import urllib2
import time
import lcd
ssid_name = "project"
ssid_password = "project8125"
def Connect_wifi():
	while(1):
		try:
			lcd.stringlcd(0x80,"Checking Internet")
			urllib2.urlopen("http://google.com")
		except urllib2.URLError as e:
			print(e.reason)
			print("No Internet connection")
			lcd.stringlcd(0x80,"No Internet")
			inf = os.popen('sudo cat /etc/wpa_supplicant/wpa_supplicant.conf').read()
			print inf
			if ((ssid_name in inf) & (ssid_password in inf)):
				print 'already found ssid '
			else:
				print 'ssid not registed adding in to network list'
				os.system("echo \'network={\' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")
				os.system("echo \'  ssid=\"" + ssid_name + "\"' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")
				os.system("echo \'  psk=\"" + ssid_password+ "\"' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")
				os.system("echo \'}\r\n\' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")

			#os.system("sudo ifdown wlan0")
			os.system("sudo ifup wlan0")
			print("Connecting..")
			lcd.stringlcd(0x80,"Connecting..")
			time.sleep(5)
		else:
			print("Up and Running")
			break
	print("wifi connecting completed")
	lcd.stringlcd(0x80,"Connected")
