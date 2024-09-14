from button.button import Button
from display.display import Display
from alarm.alarm import Alarm
import RPi.GPIO as GPIO
import time
from datetime import datetime
from subprocess import run
from enum import Enum
# import logging
# import mylib
# logger = logging.getLogger(__name__)

# def main():
#     logging.basicConfig(filename='myapp.log', level=logging.INFO)
#     logger.info('Started')
#     mylib.do_something()
#     logger.info('Finished')

PIN1= 6
PIN2 = 5

class States(Enum):
    DEFAULT = 0
    SLEEP = 1
    WAKE = 2
    ALARM = 3
    


display = Display()
state = States.DEFAULT
run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --transform 270", shell=True)

morning_alarm = Alarm()
morning_alarm.init("Good_MorningV2.mp3")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
button1 = Button(PIN1)
button2 = Button(PIN2)

button1.init_button()
button2.init_button()

print("Running")
#morning_alarm.play_alarm()
while True:
    morning_alarm.activate(19, 25)
    print("State is", state)

    match state:
        # screen and leds on are on alarm is not playing
        case States.DEFAULT:
            if button1.press(): # display and leds turn off
                state = States.SLEEP
                print(f"Button 1 pressed: Display is turning off: state is {state}")
                display.turn_off_display()
                time.sleep(0.5)

            elif morning_alarm.is_active():
                state = States.ALARM
                print("Alarm is playing")
                time.sleep(0.5)

        # screen and leds are off       
        case States.SLEEP:
            if state == States.SLEEP:
                print("Sleep State")
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
                state = States.DEFAULT
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


    
    

    

