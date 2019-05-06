'''
Author: Adam Novak

Description: This code is a stub that can be expanded to add motion to the robot.

Instructions: Place motion commands after the print('begin') and before the print('end')

Date modified: 04/24/19
Version: 1.0
Environment: Python 3.7
'''
'''
+x is away from base
+y is towards power cable side of base
+z is upwards
speed is [0, 100] if version is 4.0+
speed is [0, 100000] if 3.0 < version < 4.0

x (mm)          :  150 -> 300
y (mm)          : -150 -> 150 
z (mm)          :   30 -> 150 
speed (mm/s?)   :    0 -> 100
'''


import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from uarm.wrapper import SwiftAPI
swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
swift.waiting_ready(timeout=3)
device_info = swift.get_device_info()
print(device_info)
firmware_version = device_info['firmware_version']
#if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
#    swift.set_speed_factor(0.0005)

#set for general mode
swift.set_mode(0)

#LED pin numbers
red = 50
yellow = 45
green = 49

speed = 10
swift.reset(wait=True, speed=speed)
#swift.set_digital_output(pin=TODO, value=1) # set led based on program type

swift.flush_cmd()
print('Begin')

swift.set_position(x=200, y=23, z=100, speed=speed, wait=False)
swift.set_position(x=200, y=136, z=100, speed=speed, wait=False)
swift.set_position(x=200, y=142, z=100, speed=speed, wait=False)
swift.set_position(x=200, y=150, z=100, speed=speed, wait=False)
swift.set_position(x=150, y=127, z=30, speed=speed, wait=False)
swift.set_position(x=300, y=145, z=150, speed=speed, wait=False)


print('Ending')
swift.reset(wait=True, speed=speed)
#swift.set_digital_output(pin=TODO, value=0) # set led based on program type
swift.flush_cmd()
time.sleep(5)
swift.disconnect()
print('Finished')