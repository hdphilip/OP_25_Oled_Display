#!/usr/bin/env python
import json
from time import sleep
from luma.core.virtual import terminal
from luma.core.interface.serial import i2c
from PIL import ImageFont
from luma.oled.device import sh1106   # change to ssd1306 for different display
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
import os

# Initialize GPIO for LEDs
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)   # Green LED
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)   # Yellow LED
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)   # Red LED

# OLED Display Setup
serial = i2c(port=1, address=0x3c)
device = sh1106(serial, rotate=0)   # change to ssd1306 for different display
font = ImageFont.truetype("FreeSans.ttf", 18)  # make sure font file is in the same folder
term = terminal(device, font)
device.contrast(128)   # controls brightness 0-255

# Path to the JSON file
json_file_path = "/home/pi/op25/op25/gr-op25_repeater/apps/T_display.json"  # Make sure the path is correct    /home/pi/op25/op25/gr-op25_repeater/apps

def update_display_and_leds(metadata):
    """
    Updates the OLED display and controls LEDs based on the metadata.
    """
    # Replace idle status with 'Stand By'
    display_data = metadata.replace("[idle]", "Stand By")
    
    # Update OLED display
    term.println(display_data)
  #  print("Display Metadata: %s" % display_data)

    # Control LEDs based on metadata content
    if display_data == "GLT PD1":       
        GPIO.output(11, GPIO.HIGH)  # Turn on Green LED
    else:
        GPIO.output(11, GPIO.LOW)   # Turn off Green LED

    if display_data == "SSD 3":
        GPIO.output(13, GPIO.HIGH)  # Turn on Yellow LED
    else:
        GPIO.output(13, GPIO.LOW)   # Turn off Yellow LED

    if display_data == "C FD DSP A":
        GPIO.output(15, GPIO.HIGH)  # Turn on Red LED
    else:
        GPIO.output(15, GPIO.LOW)   # Turn off Red LED

def read_json_metadata(file_path):
    """
    Reads the metadata from the specified JSON file.
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                return data.get("metadata", "[idle]")  # Default to "[idle]" if no metadata found
        except json.JSONDecodeError:
            print("Error: Could not decode JSON.")
            return "[idle]"
    else:
        print(f"Error: {file_path} does not exist.")
        return "[idle]"

while True:
    # Read metadata from the JSON file
    metadata = read_json_metadata(json_file_path)

    # Update the OLED display and LEDs with the current metadata
    update_display_and_leds(metadata)
    
    # Sleep for a bit before checking again
    sleep(.5)
