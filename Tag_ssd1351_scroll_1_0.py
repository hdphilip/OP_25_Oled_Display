#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import subprocess
import socket
from luma.core.virtual import terminal
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1351
from PIL import ImageFont
from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
serial = spi(device=0, port=0, gpio=GPIO)
device = ssd1351(serial)

UDP_IP = "127.0.0.1"
UDP_PORT = 28002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

font = ImageFont.truetype("FreeSans.ttf", 18)  # make sure font file is in the same folder
term = terminal(device, font)
device.contrast(128) # adjust for brightness 0-255


while True:
     
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    tagdata = data.decode('utf')
    tagdata = tagdata.replace("[idle]","Stand By")   
    term.println(str(tagdata))
    print("Alfa Tag: %s" % tagdata)
    
   