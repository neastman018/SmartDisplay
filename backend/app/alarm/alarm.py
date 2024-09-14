"""
Methods for setting and activating an alarm
"""
import multiprocessing
import pygame
from datetime import datetime 
import string

"""
Function to inteperate time 
"""
#def interperate_time(time):

"""
Method to initalize the alarm
@parameter alarm_sound: music file to play
"""

"""
Method to play the alarm
@param alarm: return of the init_alarm function which is a initalized alarm with a song loaded
"""

class Alarm:

    def __init__(self, alarm = pygame.mixer.music, last_played_min=0):
        self.alarm = alarm
        pygame.mixer.init()
        self.last_played_min = last_played_min



        


    def init(self, alarm_sound):
        self.alarm.load("backend/app/alarm/music/" + alarm_sound)

        print(f"Alarm playing {alarm_sound} is ready")
    
    """
    Getter Method for the alarm being active
    @return true if alarm is playing and false if not
    """
    def is_active(self) -> bool:
        return self.alarm.get_busy()
    

    def play_alarm(self):
        self.alarm.play()
        
    """
    Plays the alarm at a certain time
    @param hour, minute is the time to play
    """
    def activate(self, hour, minute) -> bool:
        now = datetime.now()
        if hour == now.hour and minute == now.minute and not self.is_active() and now.minute != self.last_played_min:
            print(self.is_active())
            self.alarm.play()
            self.last_played_min = now.minute
            print("Alarm is playing")
    
    # Method to stop the alarm if active
    def alarm_stop(self)->bool:
        if self.is_active():
            self.alarm.stop()

if __name__ == "__main__":
    alarm  = Alarm()
    alarm.init("Good_MorningV2.mp3")
    alarm.play_alarm()
    while alarm.is_active():
        continue




          
           
    
