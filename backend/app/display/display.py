
from subprocess import run

class Display:

    def __init__(self, state = True):
        self.state = state

    def turn_on_display(self):
        run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --on", shell=True)
        self.state = True
        return True

    def turn_off_display(self):
        run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --off", shell=True)
        self.state = False
        return False
    

if __name__ == "__main__":
    display1 = Display()
    display1.turn_off_display()
