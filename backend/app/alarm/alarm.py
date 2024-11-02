"""
Methods for setting and activating an alarm
"""

import pygame
from datetime import datetime
# from logs.logs import log

class Alarm:
    def __init__(self, last_played_min=0):
        pygame.mixer.init()
        self.last_played_min = last_played_min
        self.alarm_sound = None  # Store the file path of the alarm sound

    def init(self, alarm_sound):
        # Store the alarm sound file path
        self.alarm_sound = "backend/app/alarm/music/" + alarm_sound
        print(f"Alarm sound {alarm_sound} is ready")
        # log(f"Alarm sound {alarm_sound} is ready")

    def is_active(self) -> bool:
        # Checks if the music is currently playing
        return pygame.mixer.music.get_busy()

    def play_alarm(self):
        if self.alarm_sound:
            pygame.mixer.music.load(self.alarm_sound)
            pygame.mixer.music.play()
        else:
            print("Alarm sound not initialized.")
            # log("Attempted to play alarm without initializing sound.")

    def activate(self, hour, minute) -> bool:
        now = datetime.now()
        if (
            hour == now.hour
            and minute == now.minute
            and not self.is_active()
            and now.minute != self.last_played_min
        ):
            self.play_alarm()
            self.last_played_min = now.minute
            # log(f"Alarm played at {now.hour}:{now.minute}")

    def wake_up(self, times):
        # Get day of the week and adjust so Sunday is 0 and Saturday is 6
        day_of_week = datetime.now().weekday() + 1
        if day_of_week == 7:
            day_of_week = 0

        wake_up_time = times[day_of_week]
        wake_up_hour = int(wake_up_time.split(":")[0])
        wake_up_minute = int(wake_up_time.split(":")[1])

        self.activate(wake_up_hour, wake_up_minute)

    def alarm_stop(self) -> bool:
        if self.is_active():
            pygame.mixer.music.stop()
            # log("Alarm stopped")

if __name__ == "__main__":
    alarm = Alarm()
    alarm.init("Peaky_Blinders.mp3")
    
    while True:
        if not alarm.is_active():
            alarm.play_alarm()

    
