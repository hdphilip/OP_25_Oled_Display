#!/usr/bin/env python
from luma.core.virtual import terminal
from luma.core.interface.serial import i2c
from PIL import ImageFont
from luma.oled.device import sh1106   # change to ssd1306 for different display
import socket
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)   #   Green Led
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)   #   Yellow Led
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)   #   Red Led


serial = i2c(port=1, address=0x3c)
device = sh1106(serial, rotate=0)   # change to ssd1306 for different display

UDP_IP = "127.0.0.1"
UDP_PORT = 28003

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

font = ImageFont.truetype("FreeSans.ttf", 18)  # make sure font file is in the same folder
term = terminal(device, font)
device.contrast(64) # adjust for brightness 0-255

while True:
     
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    tagdata = data.decode('utf')
    tagdata = tagdata.replace("[idle]","Stand By")   
    term.println(str(tagdata))
    print("Alfa Tag: %s" % tagdata)
    if (tagdata == "GLT PD1"):       #
        GPIO.output(11, GPIO.HIGH) # Turn on Green
    elif (tagdata != "Glt PD1"):
        GPIO.output(11, GPIO.LOW)  # Turn off Green
    if (tagdata == "SSD 3"):
        GPIO.output(13, GPIO.HIGH) # Turn on Yellow
    elif (tagdata != "SSD 3"):
        GPIO.output(13, GPIO.LOW)  # Turn off Yellow
    if (tagdata == "C FD DSP A"):
        GPIO.output(15, GPIO.HIGH) # Turn on Red
    elif (tagdata != "C FD DSP A"):
        GPIO.output(15, GPIO.LOW)  # Turn off Red  



    
        


    
        