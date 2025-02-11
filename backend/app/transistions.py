"""
File to hold all the different state transitions
"""
from button.button import Button
from display.display import Display
import RPi.GPIO as GPIO
import time
from datetime import datetime
from subprocess import run
from enum import Enum
from logs.logs import log
from alarm.alarm import Alarm
from lights.lights import LEDs



class States(Enum):
    DEFAULT = 0
    SLEEP = 1
    WAKE = 2
    ALARM = 3


#================================================================================================
#================================================================================================

def default_button1(display) -> States:

    display.turn_off_display()
    time.sleep(0.5)
    return 1

def default_button2(alarm) -> States:
    alarm.play_alarm()
    time.sleep(0.5)
    return 3

def default_encoder_button(alarm) -> States:
    alarm.play_alarm()
    time.sleep(0.5)
    return 3

def default_alarm() -> States:
    time.sleep(0.5)
    return 3

#================================================================================================
#================================================================================================

def sleep_button1(display) -> States:
    display.turn_on_display()
    time.sleep(0.5)
    return 0

def sleep_button2(alarm) -> States:
    alarm.play_alarm()
    time.sleep(0.5)
    return 3

def sleep_encoder_button(alarm) -> States:
    alarm.play_alarm()
    time.sleep(0.5)
    return 3

def sleep_alarm() -> States:
    time.sleep(0.5)
    return 3

#================================================================================================
#================================================================================================

def alarm_button1(display) -> States:
    display.turn_off_display()
    return 3

def alarm_button2(alarm) -> States:
    alarm.alarm_stop()
    time.sleep(0.5)
    return 0

def alarm_alarm_end(alarm) -> States:  
    alarm.play_alarm(alarm)
    time.sleep(0.5)
    return 3

#================================================================================================
#================================================================================================



