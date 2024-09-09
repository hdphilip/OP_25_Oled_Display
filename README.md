# OP_25_Oled_Display

This project Displays the OP25 Alfa  Tags on a OLED Display

<img src="https://github.com/hdphilip/OP_25_Oled_Display/blob/main/Pictures/ssh1106.jpg" width=300 align="left">

<img src="https://github.com/hdphilip/OP_25_Oled_Display/blob/main/Pictures/ssd1351.jpg" width=300 align="left">

<img src="https://github.com/hdphilip/OP_25_Oled_Display/blob/main/Pictures/ssd1306.jpg" alt="drawing" style="width:200px;"/>

This is a Work in Progress,
as you can see from my code, I am a beginner and I welcome changes, this could be a fun project!!!

For more information, check out Radio Reference:
 <https://forums.radioreference.com/threads/op25-boatbod-update.430476/#post-3562825>

special thanks must be given to “BoatBod, KA1RBI and many others for the work they have done on the project.

Who is this project intended for?

Raspberry Pi owners who like to experiment on connecting different hardware devices up to their Pi and using software like “VScode” or “Thonny” to make them work.

Here are the steps:

It’s best to practice the installation on a spare micro SD card with a working OP25, liquid soap. So you are able to open up a VLC player and listen to the audio and see the alfa tags on the upper left hand corner. (my setup was using rx.py) I haven’t tried it on the other types.

Step 1:

Wire up your display (i2c) to your raspberry Pi, 4 wires +3, GND, SCL, SCK

Install Luma.oled drivers :


<https://luma-oled.readthedocs.io/en/latest/hardware.html>

after you have finished it’s time to install the samples:

<https://github.com/rm-hull/luma.examples>

And run them!!!! some are pretty cool
And run them in Thonny!  
(Hint for Thonny, use the Program arguments for the command line ) I used -d sh1106 (might work without it.)

Here are the steps:

It’s best to practice the installation on a spare micro SD card with a working OP25 with liquid soap. So you are able to open up a VLC player and listen to the audio and see the alfa tags on the upper left hand corner. (my setup was using rx.py) I haven’t tried it on the other types.
Step 1:
Wire up your display (i2c) to your raspberry Pi, 4 wires +3, GND, SCL, SCK
Install Luma.oled drivers :

<https://luma-oled.readthedocs.io/en/latest/hardware.html>

after you have finished,  it’s time to install the samples,

<https://github.com/rm-hull/luma.examples>

And run them in Thonny!

ya need to verify the oled is working!

(Hint for Thonny, use the Program arguments for the command line ) I used -d sh1106 (might work without it.)

Now here is the most important part.
Replace the 'icemeta.py'.

Notes:

If the icemeta replacement is working, you should see the T_display.json change, (i use vscode) when the metadata changes.

In the T_oled.py , you'll see where i have have it control some LED's.  

Also make sure you put the font file in the same directory as T_oled.py".py
Put it in the same dir as icemeta.py

If all goes well, start op25 with liquidsoap, open Thonny, open and run the tag oled display file, and wait for a call to display, you can make changes to the tag display file without restarting op25.

Very important!!!!

**Delete the icemeta.pyc file, a new one will be created next run time.**

If you get a error, i just rebooted. 

If a new .pyc file was not created look at the error output file to see what went wrong, this will help you troubleshoot.

The display drivers were a real pain at first..

hopefully i didn"t forget anything...lol
Good Luck
