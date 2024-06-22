"""
Button Class
"""

import time
import RPi.GPIO as GPIO

class Button:
    """
    @parameter pin is the GPIO pin the button is hooked up to (pin number on board)
    @parameter state is whichever state variable the button is controlling
    @parameter last_press in the time of the last button press for debounce purposes
    """
    def __init__(self, pin = 0, state = False, pressed = False, last_press = time.time(), debounce : float  = 0.1):
        self.pin = pin
        self.state = state
        self.pressed = pressed
        self.last_press = last_press
        self.debounce = debounce
        self.button = None
        """
        Method to inialize the button
        @parameter pin is the pin number that the button is hooked up to
        """
    def init_button(self):
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    """
    Method that will return a true false based on the state of the button press
    Button will act like a switch

    """ 
    def switch(self) -> bool:
        if GPIO.input(self.pin) == GPIO.HIGH and (time.time() - self.last_press) >= self.debounce and not self.pressed:
            self.pressed = True
            self.last_press = time.time()
            self.state = not self.state

        if GPIO.input(self.pin) == GPIO.LOW and (time.time() - self.last_press) >= self.debounce:
            self.pressed = False

        return self.state
    


    def press(self) -> bool:
        if GPIO.input(self.pin) == GPIO.HIGH and (time.time() - self.last_press) >= self.debounce and not self.pressed:
            self.pressed = True
            self.last_press = time.time()

        elif GPIO.input(self.pin) == GPIO.LOW and (time.time() - self.last_press) >= self.debounce:
            self.pressed = False

        return self.pressed



    """
    Method to test button press
    """
    def test_press(self) -> bool:
        press = self.press()
        return press

    """
    Method to test button switch
    """
    def test_switch(self) -> bool:
        switch = self.state
        if (self.switch() != switch):
            switch = self.state
            print(self.state)
        return switch



"""
Runs when file runs to test button methods
"""
if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    button1 = Button(pin=14)
    button1.init_button()

    while True:
        button1.test_switch()


