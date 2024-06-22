"""
File to do a test run on computer
"""
from datetime import datetime

hour = datetime.now().hour
minute = datetime.now().minute
second = datetime.now().second
print("Test run at: ", hour, ":", minute)