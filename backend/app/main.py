from button.button import Button
from display.display import Display
from alarm.alarm import Alarm
import RPi.GPIO as GPIO
import time

PIN1= 6
PIN2 = 5

display = Display()

morning_alarm = Alarm()
morning_alarm.init("Good_MorningV2.mp3")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
button1 = Button(PIN1)
button2 = Button(PIN2)

button1.init_button()
button2.init_button()

print("Running")

while True:

    morning_alarm.activate(23, 8)

    if button2.press() and morning_alarm.is_active():
        morning_alarm.alarm_stop()

    if button1.press() and display.state:
        print("Button 1 pressed: Display is turning off")
        display.turn_off_display()
        time.sleep(0.5)

    elif button1.press() and not display.state:
        print("Button 1 pressed: Display is turning on")
        display.turn_on_display()
        time.sleep(0.5)


    
    

    

