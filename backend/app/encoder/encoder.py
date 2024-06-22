"""
Class for a rotary encoder
"""

import Encoder
from time import sleep
import RPi.GPIO as GPIO


GPIO.setMode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)

encoder = Encoder.Encoder(20, 21)

while True:
    print(encoder.read())
    sleep(0.1)

