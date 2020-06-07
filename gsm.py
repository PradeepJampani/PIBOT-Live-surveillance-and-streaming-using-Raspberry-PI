import time
import serial
ser = serial.Serial('/dev/ttyS0',9600)

def Gsminit():
	ser.write('AT\r\n')
	print'AT'
	time.sleep(1)
	ser.write('AT+CMGF=1\r\n')
	print'AT+CMGF=1'
	time.sleep(1)
	ser.write('AT+CNMI=1,2,0,0\r\n')
	print'AT+CNMI=1,2,0,0'
	time.sleep(1)
	print'Initilized'
	return

def Sendmsg(num,msg):
	ser.write('AT+CMGS=\"' + num + '\"\r\n')
	print num
	time.sleep(2)
	ser.write(msg)
	print msg
	ser.write(serial.to_bytes([0x1a]))
	return
