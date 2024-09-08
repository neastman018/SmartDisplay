from subprocess import run


run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --transform 270", shell=True)
run("cd backend && python3 app/main.py", shell=True)
run("cd frontend && npm run start", shell=True)