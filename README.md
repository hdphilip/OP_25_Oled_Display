# OP_25_Oled_Display
This project Displays the OP25 Alfa  Tags on a OLED Display

This is a Work in Progress,
as you can see from my code, i am a beginner 
  
For more information, check out Radio Reference:
 https://forums.radioreference.com/threads/op25-boatbod-update.430476/#post-3562825
special thanks must be given to “BoatBod, KA1RBI and many others for the work they have done on the project.

Who is this project intended for?

Raspberry Pi owners who like to experiment on connecting different hardware devices up to their Pi and using software like “VScode” or “Thonny” to make them work.

Here are the steps:

It’s best to practice the installation on a spare micro SD card with a working OP25, liquid soap. So you are able to open up a VLC player and listen to the audio and see the alfa tags on the upper left hand corner. (my setup was using rx.py) I haven’t tried it on the other types.
Step 1:
Wire up your display (i2c) to your raspberry Pi, 4 wires +3, GND, SCL, SCK 
Install Luma.oled drivers :
https://luma-oled.readthedocs.io/en/latest/hardware.html
after you have finished it’s time to install the samples,
https://github.com/rm-hull/luma.examples
and run them!!!!
And run them in Thonny!  
(Hint for Thonny, use the Program arguments for the command line ) I used -d sh1106 (might work without it.)

Here are the steps:

It’s best to practice the installation on a spare micro SD card with a working OP25 with liquid soap. So you are able to open up a VLC player and listen to the audio and see the alfa tags on the upper left hand corner. (my setup was using rx.py) I haven’t tried it on the other types.
Step 1:
Wire up your display (i2c) to your raspberry Pi, 4 wires +3, GND, SCL, SCK 
Install Luma.oled drivers :
https://luma-oled.readthedocs.io/en/latest/hardware.html
after you have finished it’s time to install the samples,
https://github.com/rm-hull/luma.examples
and run them!!!!
And run them in Thonny!  
(Hint for Thonny, use the Program arguments for the command line ) I used -d sh1106 (might work without it.)



