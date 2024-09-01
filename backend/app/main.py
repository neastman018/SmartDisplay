from button.button import Button
from display.display import Display
import RPi.GPIO as GPIO

PIN1= 5
PIN2 = 6

display = Display()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
button1 = Button(PIN1)
button2 = Button(PIN2)

button1.init_button()
button2.init_button()

while True:
    if button1.press() and display.state:
        print("Button 1 pressed: Display is turning off")
        display.turn_off_display()
    elif button1.press() and not display.state:
        print("Button 1 pressed: Display is turning on")
        display.turn_on_display()
    

    

