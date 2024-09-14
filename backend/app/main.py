from button.button import Button
from display.display import Display
from alarm.alarm import Alarm
import RPi.GPIO as GPIO
import time
from datetime import datetime
from subprocess import run
from enum import Enum



PIN1= 6
PIN2 = 5

class States(Enum):
    DEFAULT = 0
    SLEEP = 1
    WAKE = 2
    ALARM = 3
    


display = Display()
state = States.DEFAULT

morning_alarm = Alarm()
morning_alarm.init("Good_MorningV2.mp3")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
button1 = Button(PIN1)
button2 = Button(PIN2)

button1.init_button()
button2.init_button()

run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --transform 270", shell=True)
print("Running")
#morning_alarm.play_alarm()
while True:
    morning_alarm.activate(8, 43)

    match state:
        # screen and leds on are on alarm is not playing
        case States.DEFAULT:
            if button1.press(): # display and leds turn off
                states = States.SLEEP
                print("Button 1 pressed: Display is turning off")
                display.turn_off_display()
                time.sleep(0.5)

            elif morning_alarm.is_active():
                states = States.ALARM
                print("Alarm is playing")
                time.sleep(0.5)

        # screen and leds are off       
        case States.SLEEP:
            if button1.press():
                states = States.DEFAULT
                print("Button 1 pressed: Display is turning on")
                display.turn_on_display()
                time.sleep(0.5)
            
            
        case States.WAKE:
            print("Wake State")

        # Alarm is playing    
        case States.ALARM:

            if button2.press():
                morning_alarm.alarm_stop()
                states = States.DEFAULT
                print("Alarm stopped")
                time.sleep(0.5)
            

    # if button1.press() and display.state:
    #     print("Button 1 pressed: Display is turning off")
    #     display.turn_off_display()
    #     time.sleep(0.5)

    # elif button1.press() and not display.state:
    #     print("Button 1 pressed: Display is turning on")
    #     display.turn_on_display()
    #     time.sleep(0.5)


    
    

    

