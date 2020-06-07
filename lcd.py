import RPi.GPIO as GPIO
import time
 
# Define GPIO to LCD mapping
LCD_RS = 33
LCD_E  = 35
LCD_D4 = 37
LCD_D5 = 40
LCD_D6 = 38
LCD_D7 = 36
 
# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
 
# Timing constants
E_PULSE = 0.001
E_DELAY = 0.001
 
def lcd_init():
  # Initialise display
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E,GPIO.OUT)  # E
  GPIO.setup(LCD_RS,GPIO.OUT) # RS
  GPIO.setup(LCD_D4,GPIO.OUT) # DB4
  GPIO.setup(LCD_D5,GPIO.OUT) # DB5
  GPIO.setup(LCD_D6,GPIO.OUT) # DB6
  GPIO.setup(LCD_D7,GPIO.OUT) # DB7
 
  lcd_byte(0x02,LCD_CMD) # 110011 Initialise
  lcd_byte(0x02,LCD_CMD)
  lcd_byte(0x28,LCD_CMD) # 110010 Initialise
  lcd_byte(0x28,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0e,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x06,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def stringlcd(cmd,message):
	print('LCD:' + message)
	if(cmd == 0x80):
		lcd_byte(0x01, LCD_CMD)
	lcd_byte(cmd, LCD_CMD)
	for i in range(len(message)):
		lcd_byte(ord(message[i]),LCD_CHR)
	if(len(message) > 16):
		lcd_byte(0xc0, LCD_CMD)
		for i in range(len(message)-16):
			lcd_byte(ord(message[i+16]),LCD_CHR)
		
  
 
def endgpio():
   GPIO.cleanup()
