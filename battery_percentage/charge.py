# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 23:12:27 2021

@author: nkele
"""

import psutil
# from plyer import notification
import time

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

while (True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    
    print("Battery Remaining : %d" % (percent))
    print("Power plugged in : ", battery.power_plugged)
    print("Battery left : ", convertTime(battery.secsleft))
    
    time.sleep(60)
    
    continue
    