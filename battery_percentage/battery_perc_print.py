
import psutil
from plyer import notification
import time

while (True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    
    print("Battery Remaining : %d" % (percent))
    
    time.sleep(60)
    
    continue
    
