from __future__ import division
import lcd
import RPi.GPIO as GPIO
import spidev
import time

def bitstring(n):
    s = bin(n)[2:]
    return '0'*(8-len(s)) + s

def read(adc_channel=0, spi_channel=0):
    conn = spidev.SpiDev(0, spi_channel)
    conn.max_speed_hz = 50000 # 1.2 MHz
    cmd = 128 + 64
    if adc_channel:
        cmd += 32
    reply_bytes = conn.xfer2([cmd, 0])
    reply_bitstring = ''.join(bitstring(n) for n in reply_bytes)
    reply = reply_bitstring[5:15]
    #print reply
    return int(reply, 2)# / 2**10

