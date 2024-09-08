from subprocess import run
from threading import Thread

def run_script(script_name):
    run(["python", script_name])

if __name__ == "__main__":

    run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --transform 270", shell=True)

    t1 = Thread(target=run_script, args=("backend/app/main.py",))
    t2 = Thread(target=run_script, args=("frontend/node_modules/.bin/react-scripts start",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
