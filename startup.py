from subprocess import run
from threading import Thread

def run_script(script_name):
    run(script_name, shell=True)

if __name__ == "__main__":

    t1 = Thread(target=run_script, args=("python backend/app/main.py",))
    t2 = Thread(target=run_script, args=("cd frontend && npm run start",))
    run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --transform 270", shell=True)


    t1.start()
    t2.start()
    t1.join()
    t2.join()
