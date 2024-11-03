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
    return States.SLEEP

def default_button2(alarm) -> States:
    alarm.play_alarm()
    time.sleep(0.5)
    return States.ALARM

def default_alarm() -> States:
    time.sleep(0.5)
    return States.ALARM

#================================================================================================
#================================================================================================

def sleep_button1(display) -> States:
    display.turn_on_display()
    time.sleep(0.5)
    return States.DEFAULT

def sleep_button2(alarm) -> States:
    alarm.play_alarm()
    time.sleep(0.5)
    return States.ALARM

def sleep_alarm() -> States:
    time.sleep(0.5)
    return States.ALARM

#================================================================================================
#================================================================================================

def alarm_button1(display) -> States:
    display.turn_off_display()
    return States.ALARM

def alarm_button2(alarm) -> States:
    alarm.stop_alarm()
    time.sleep(0.5)
    return States.DEFAULT

def alarm_alarm_end() -> States:
    time.sleep(0.5)
    return States.DEFAULT

#================================================================================================
#================================================================================================



