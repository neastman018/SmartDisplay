from button.button import Button
from display.display import Display
import RPi.GPIO as GPIO
import time
from datetime import datetime
from subprocess import run
from enum import Enum
from logs.logs import log
from alarm.alarm import Alarm

#Test Comment, this can be delelted
PIN1= 6
PIN2 = 5
ROTARY_PIN = 4

class States(Enum):
    DEFAULT = 0
    SLEEP = 1
    WAKE = 2
    ALARM = 3

wake_up_times = ["8:40", "6:15", "6:15", "6:15", "6:15", "6:15", "7:30"]    


display = Display()
state = States.DEFAULT


morning_alarm = Alarm()
morning_alarm.init("Peaky_Blinders.mp3")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
button1 = Button(PIN1)
button2 = Button(PIN2)

button1.init_button()
button2.init_button()

print("Running")
log("Backend has started")


while True:
    morning_alarm.wake_up(wake_up_times)

    
    match state:
        # screen and leds on are on alarm is not playing
        case States.DEFAULT:
            if button1.press(): # display and leds turn off
                state = States.SLEEP
                print(f"Button 1 pressed: Display is turning off: state is {state}")
                log(f"Button 1 pressed: Display is turning off: state is {state}")
                display.turn_off_display()
                time.sleep(0.5)

            elif morning_alarm.is_active():
                state = States.ALARM
                log(f"Should switch to State.ALARM and Switching to {state}")
                time.sleep(0.5)

        # screen and leds are off       
        case States.SLEEP:
            if button1.press():
                state = States.DEFAULT
                print("Button 1 pressed: Display is turning on")
                log(f"Button 1 pressed: Display is turning on: state is {state}")
               
                display.turn_on_display()
                time.sleep(0.5)
            
            elif morning_alarm.is_active():
                state = States.ALARM
                display.turn_on_display()
                log(f"Should switch to State.ALARM and Switching to {state}")
                time.sleep(0.5)
            
            
        case States.WAKE:
            print("Wake State")

        # Alarm is playing    
        case States.ALARM:

            if button2.press():
                morning_alarm.alarm_stop()
                state = States.DEFAULT
                print("Alarm stopped")
                log(f"Button 2 pressed: Alarm stopped. Switching to {state}")
                time.sleep(0.5)
            


