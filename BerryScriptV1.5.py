import os

from gpiozero import PWMLED
from gpiozero import RGBLED 
from time import sleep

SINGLEled = PWMLED(2)
led = RGBLED(17, 4, 3)
DO_NOT_USE = os.system('clear')


print(" ░▒▓▓▓▓▓▓▒░░▒▓▓▓▓▓▓▒░")
print(" ░█▓▓▓▓▓▓▓██▓▓▓▓▓▓▓█░")
print(" ░░█▓▓▓▓▓████▓▓▓▓▓█▒░")
print(" ░░░▓█▓██████████▓░░░")
print(" ░░▓██████████████▓░░")
print(" ░░████████████████░░")
print(" ▒██████████████████▒")
print(" ████████████████████")
print(" ▒██████████████████▒")
print(" ░▓████████████████▓░")
print(" ░░▓██████████████▓░░")
print(" ░░░░▒▓████████▓▒░░░░")
print("")
print("+-------------------+")
print("|     WELCOME TO    |")
print("|                   |")
print("|    BERRYSCRIPT    |")
print("+-------------------+")
print("")
print("")

print("HELLO USER. IN ORDER TO PERSONALISE YOUR EXPERIANCE, PLEASE ENTER YOUR NAME BELOW")

name = input("")

while True :
    
    # GETS USER INPUT
    i = input("ENTER COMMAND >>")
    
    #COMPARES IT AGAINST THIS LIST OF COMMANDS
    
    if i == "HELP" :
        print("+----------------+")
        print("|LIST OF COMMANDS|")
        print("|      HELP      |")
        print("|      EXIT      |")
        print("|   LED FADE ON  |")
        print("|   LED FADE OFF |")
        print("|       RED      |")
        print("|      GREEN     |")
        print("|      BLUE      |")
        print("|      YELLOW    |")
        print("|      CYAN      |")
        print("|      MAGENTA   |")
        print("|      WHITE     |")
        print("|      BLACK     |")
        print("|      CLEAR     |")
        print("+----------------+")
    else :
        if i == "EXIT" :
            
            print("See You Later,", )
            
            exit()
        else :
            if i == "LED FADE ON" :
                SINGLEled.value = 0.0
                sleep(0.2)
                SINGLEled.value = 0.2
                sleep(0.2)
                SINGLEled.value = 0.4
                sleep(0.2)
                SINGLEled.value = 0.6
                sleep(0.2)
                SINGLEled.value = 0.8
                sleep(0.2)
                SINGLEled.value = 1
            else :
                if i == "LED FADE OFF" :
                    SINGLEled.value = 1
                    sleep(0.2)
                    SINGLEled.value = 0.8
                    sleep(0.2)
                    SINGLEled.value = 0.6
                    sleep(0.2)
                    SINGLEled.value = 0.4
                    sleep(0.2)
                    SINGLEled.value = 0.2
                    sleep(0.2)
                    SINGLEled.value = 0
                else :
                    if i == "RED" :
                        led.color = (1, 0, 0)
                    else :
                        if i == "GREEN" :
                            led.color = (0, 1, 0)
                        else :
                            if i == "BLUE" :
                                led.color = (0, 0, 1)
                            else :
                                if i == "YELLOW" :
                                    led.color = (1, 1, 0)
                                else :
                                    if i == "CYAN" :
                                        led.color = (0, 1, 1)
                                    else :
                                        if i == "MAGENTA" :
                                            led.color = (1, 0, 1)
                                        else :
                                            if i == "WHITE" :
                                                led.color = (1, 1, 1)
                                            else :
                                                if i == "BLACK" :
                                                    led.color = (0, 0, 0)
                                                else :
                                                    
                                                    print("HELLO,",name,".")
                                                    print("THE CREATOR HAS JUST SENT YOU A MESSAGE AND WILL BE RENDERED SHORTLY.")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    
                                                    
                                                    sleep (5)
                                                    print("+----------------------------------------------------------+")
                                                    sleep (0.1)
                                                    print("|                          ERROR                           |")
                                                    sleep (0.1)
                                                    print("|                 I AM SORRY TO SAY THIS,                  |")
                                                    sleep (0.1)
                                                    print("|                BUT WHAT YOU JUST ENTERED                 |")
                                                    sleep (0.1)
                                                    print("|                 IS NOT A VALID COMMAND!                  |")
                                                    sleep (0.1)
                                                    print("|                                                          |")
                                                    sleep (0.1)
                                                    print("|            IF YOU NEED HELP,I AM ALWAYS HERE,            |")
                                                    sleep (0.1)
                                                    print("|          JUST TYPE HELP FOR A LIST OF COMMANDS           |")
                                                    sleep (0.1)
                                                    print("|                                                          |")
                                                    sleep (0.1)
                                                    print("|             HAPPY COIDNG, FROM THE CREATOR,              |")
                                                    sleep (0.1)
                                                    print("|                         JOSEPH                           |")
                                                    sleep (0.1)
                                                    print("|                                                          |")
                                                    sleep (0.1)
                                                    print("+----------------------------------------------------------+")
                                                    sleep (0.1)
                                                    
                                                    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                                                    sleep(0.5)
                                                    print("░░░▒▒▒▒▒░░▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                                                    sleep(0.5)
                                                    print("░░░░░░░░░░░▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                                                    sleep(0.5)
                                                    print("░░░░░░░░░░░▒▓░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░▒▒▒▓░░░░▒▒▒▒▒▒▒░░░░█▒░░▒▒▓░░░░░░░░░░░░░░░░░░░░░░░░░")
                                                    sleep(0.5)
                                                    print("░░░░░░░░░░░░█░░░░▒▓▒▒▒▓▓░░░░░▓░░░░░░░▒▓░░░▒▒░░░▓░░░░░░▒▓░░█░░░░░░▓▒░░░░░░░░░░░░░░░░░░░░░░░")
                                                    sleep(0.5)
                                                    print("░░░░░▓▒░░░░░▓▒░░░█▒░░░░░█░░░░▒▓▒▓▒░░░▓▓▒▒▒░░░░░▒▒░░░░░▒▓░░█░░░░░░▒▓░░░░░░░░░░░░░░░░░░░░░░░")
                                                    sleep(0.5)
                                                    print("░░░░░░▒▓▓▓▒▓▒░░░░░▓▓▒▒▓▓░░░░░░░▒▒▓▒░░░▓▒▒▒▒▓░░░▒▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                                                    sleep(0.5)
                                                    print("░░░░░▓▓▓▒░▒▓▓░░░░▒▒░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░▒▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                                                    sleep(0.5)
                                                    print("░░░░░░░░▒▓░░░▓▒▓▓▒▒▓▒▓▓▓▒▒▓█▒░░░▒▒░░▒▓▒░░▒▒░░▒▒▒▓░▒▒░░░▓▓▒░▒▒▒▓░░░▒░░░░░░░░░░░░░░░░░░░░░░░")
                                                    sleep(0.5)
                                                    print("░░░░░░░░░░░░░░░░░░░░▒░░░▓▒░░▓▓▒▓▒▓▓▓░░▓▓▓░▒▓▓▒░▒▓░░░▓▓▒░░░▒░░░░▓▒▓░░░░░░░░░░░░░░░░░░░░░░░░")
                                                    print("")

                                                    os.system('cls||clear')
