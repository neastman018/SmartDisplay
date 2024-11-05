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

wake_up_times = ["7:30", "6:15", "6:15", "6:15", "6:15", "6:15", "7:30"]    


display = Display()
state = States.DEFAULT


morning_alarm = Alarm()
morning_alarm.init("Peaky_Blinders.mp3")

alarm2 = Alarm()
alarm2.init("My_Way.mp3")
study_music = Alarm()
study_music.init("study_chants.mp3")
sleep_sounds = Alarm()
sleep_sounds.init("rain_noise.mp3")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
button1 = Button(PIN1)
button2 = Button(PIN2)
encoder_button = Button(ROTARY_PIN)

button1.init_button()
button2.init_button()
encoder_button.init_button()

log("Running")
log("Backend has started")

while True:
    playing_alarm = None
    morning_alarm.wake_up(wake_up_times)

    match state:
        # screen and leds on are on alarm is not playing
        case States.DEFAULT:
            if button1.press(): # display and leds turn off
                log("Button 1 pressed: Display is turning off: state is SLEEP")
                state = States(default_button1(display))

            if button2.press(): # play music
                log("Button 2 Pressed: Music Turning On")
                state = States(default_button2(morning_alarm))
                playing_alarm = morning_alarm

            if encoder_button.press():
                log("Encoder Button Pressed")
                state = States(default_encoder_button(study_music))
                playing_alarm = study_music

            elif morning_alarm.is_active():
                log("Alarm is Active")
                state = States(default_alarm())

        # screen and leds are off       
        case States.SLEEP:
            if button1.press():
                log("Button 1 pressed: Display is turning On: state is DEFAULT")
                state = States(sleep_button1(display))

            if button2.press():
                log("Button 2 Pressed: Music Turning On")
                state = States(sleep_button2(morning_alarm))
                playing_alarm = morning_alarm

            if encoder_button.press():
                log("Encoder Button Pressed")
                state = States(sleep_encoder_button(sleep_sounds))
                playing_alarm = sleep_sounds
            
            elif morning_alarm.is_active():
                log("Alarm is Active")
                state = States(sleep_alarm())
            
            
        case States.WAKE:
            log("Wake State")

        # Alarm is playing    
        case States.ALARM:
            if button1.press():
                log("Button 1 pressed: Display is turning off: state is still ALARM")
                state = States(alarm_button1(display))
            if button2.press():
                log("Button 2 Pressed: Music Turning Of")
                state = States(alarm_button2(playing_alarm))
            
            elif not playing_alarm.is_active():
                log("Alarm Finished")
                state = States(alarm_alarm_end(playing_alarm))


