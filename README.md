# BerryScript
BerryScript is an intuitive comand line made with python


# HOW TO INSTALL AND SET UP.

This program is for a raspberry pi with the gpio pins visible.

# STEP 1.

Open Terminal.


# STEP 2.

Once terminal is open copy this in by selecting it , right click, copy.

then in terminal, right click, paste.

> git clone https://github.com/josephthenerd/BerryScript.git 

Press enter.

# STEP 3A.

If you would like a hat version of this, I have a pcb you can buy here


> https://www.pcbway.com/project/shareproject/BerryScript_Hat_V1_3abdee49.html

 
otherwise you need:


4x comm. cathode rgb led

4x led of any colour

1x 150 ohm resistor

jumper wires.

# STEP 3B.

WIRING RGB LEDs.

all rgb pins share the same gpios.

red pin - gpio 17

green pin - gpio 4

blue pin - gpio 3

ground pin - any gnd pin on board

WIRING LEDs.

positive pin - gpio 2
negative pin - any gnd pin on board.

# STEP 4 

power on your  raspbery pi. The rgb leds should be blue.

To run the software, open terminal and type

python3 BerryScript.py

hit enter and you should be logged in.

# LIST OF COMMANDS

REMEMBER!!! ALL COMMANDS ARE IN CAPITALS!!!

HELP - hows a list of commands

EXIT - exits program

LED FADE ON - slowly turns on the single colour leds

LED FADE OFF - slowly turns off the single colour leds


The next comands changes the colour of the rgb leds

RED

GREEN

BLUE

YELLOW

CYAN

MAGENTA

WHITE

BLACK - turns rgb leds off
