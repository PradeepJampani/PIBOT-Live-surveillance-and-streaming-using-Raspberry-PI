import ftplib
import lcd
import time
import datetime
def sendftp(cs):
	try:
		ftpses = ftplib.FTP('ftp.filegenie.com','iotserver','iotserver')
		file = open('image.jpeg','rb')
		print('uploading file')
		ftpses.storbinary("STOR agrisystem/image_" + cs + "_" + str(datetime.datetime.now())+".jpg",file)
		file.close()
		ftpses.quit()
		print('Uploaded')
		lcd.stringlcd(0x80,"UPLOADED ")
		time.sleep(5)
	except:
		print('unable to upload')
		lcd.stringlcd(0x80,"UPLOADED FAILED")
		time.sleep(3)
