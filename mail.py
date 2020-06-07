import smtplib
import lcd
def send(to,ms): 
	lcd.stringlcd(0x80,"mail sending")
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login("raspberrysudo@gmail.com", "raspberrysudo6324")
	 
	msg = "\n".join([
	  "From: raspberrysudo@gmail.com",
	  "To: "+to,
	  "Subject: Warning.....",
	  "Date: 01/06/2016",
	  ms
	  ])
	try:
		print 'Sending Mail'
		server.sendmail("raspberrysudo@gmail.com", to, msg)
		server.quit()
		print 'Mail Sent'
		lcd.stringlcd(0x80,"MAIL SENT")
	except:
		print 'Mail Sending Failed'
		lcd.stringlcd(0x80,"Mail  Failed")
