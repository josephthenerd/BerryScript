from gpiozero import PWMLED
from gpiozero import RGBLED 
from time import sleep

SINGLEled = PWMLED(2)
led = RGBLED(17, 4, 3)

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
        print("+----------------+")
    else :
        if i == "EXIT" :
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
                                                    print("+-------------------------------------+") 
                                                    print("|                 ERROR               |")
                                                    print("|        I AM SORRY TO SAY THIS,      |")
                                                    print("|       BUT WHAT YOU JUST ENTERED     |")
                                                    print("|        IS NOT A VALID COMMAND!      |")
                                                    print("|                                     |")
                                                    print("|  IF YOU NEED HELP,I AM ALWAYS HERE, |")
                                                    print("|JUST TYPE HELP FOR A LIST OF COMMANDS|")
                                                    print("|                                     |")
                                                    print("|   HAPPY COIDNG, FROM THE CREATOR,   |")
                                                    print("|                JOSEPH               |")
                                                    print("|                                     |")
                                                    print("+-------------------------------------+")
                                                    
