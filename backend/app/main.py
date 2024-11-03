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

wake_up_times = ["7:30", "6:15", "6:15", "6:15", "6:15", "6:15", "23:59"]    


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
                state = default_button1(display)

            if button2.press(): # play music
                state = default_button2(morning_alarm)

            elif morning_alarm.is_active():
                state = default_alarm(morning_alarm)

        # screen and leds are off       
        case States.SLEEP:
            if button1.press():
                state = sleep_button1(display)

            if button2.press():
                state = sleep_button2(morning_alarm)
            
            elif morning_alarm.is_active():
                state = sleep_alarm(morning_alarm)
            
            
        case States.WAKE:
            print("Wake State")

        # Alarm is playing    
        case States.ALARM:
            if button1.press():
                state = alarm_button1(morning_alarm)
            if button2.press():
                state = alarm_button2(morning_alarm)
            


