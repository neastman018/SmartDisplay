from button.button import Button
from display.display import Display
import RPi.GPIO as GPIO
import time
from datetime import datetime
from subprocess import run
from enum import Enum
from logs.logs import log
from alarm.alarm import Alarm
from transistions import *

#Test Comment, this can be delelted
PIN1= 6
PIN2 = 5
ROTARY_PIN = 4

class States(Enum):
    DEFAULT = 0
    SLEEP = 1
    WAKE = 2
    ALARM = 3

wake_up_times = ["8:20", "6:15", "6:15", "6:15", "6:15", "6:15", "7:30"]    


display = Display()
state = States.DEFAULT


morning_alarm = Alarm()
morning_alarm.init("Peaky_Blinders.mp3")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
button1 = Button(PIN1)
button2 = Button(PIN2)
encoder_button = Button(ROTARY_PIN)

button1.init_button()
button2.init_button()
encoder_button.init_button()

print("Running")
log("Backend has started")


while True:
    morning_alarm.wake_up(wake_up_times)

    
    match state:
        # screen and leds on are on alarm is not playing
        case States.DEFAULT:
            if button1.press(): # display and leds turn off
                print("Button 1 pressed: Display is turning off: state is SLEEP")
                state = States(default_button1(display))

            if button2.press(): # play music
                print("Button 2 Pressed: Music Turning On")
                state = States(default_button2(morning_alarm))

            if encoder_button.press():
                print("Encoder Button Pressed")

            elif morning_alarm.is_active():
                print("Alarm is Active")
                state = States(default_alarm())

        # screen and leds are off       
        case States.SLEEP:
            if button1.press():
                print("Button 1 pressed: Display is turning On: state is DEFAULT")
                state = States(sleep_button1(display))

            if button2.press():
                print("Button 2 Pressed: Music Turning On")
                state = States(sleep_button2(morning_alarm))
            
            elif morning_alarm.is_active():
                print("Alarm is Active")
                state = States(sleep_alarm())
            
            
        case States.WAKE:
            print("Wake State")

        # Alarm is playing    
        case States.ALARM:
            if button1.press():
                print("Button 1 pressed: Display is turning off: state is still ALARM")
                state = States(alarm_button1(display))
            if button2.press():
                print("Button 2 Pressed: Music Turning Of")
                state = States(alarm_button2(morning_alarm))
            elif not morning_alarm.is_active():
                print("Alarm is not active: Switching to DEFAULT")
                state = States(alarm_alarm_end())
            


