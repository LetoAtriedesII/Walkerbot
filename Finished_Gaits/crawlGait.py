'''
Author: Adam Novak

Description: This code emulates CRAWLING motion. The data points were gathered by using the Grace Industries PASS sensor.

Instructions: Run the code after connecting to the uArm Swift Pro via USB. 

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

speed = 100
swift.reset(wait=True, speed=speed)
swift.set_digital_output(pin=49, value=1) # green led
swift.flush_cmd()
print('begin')


swift.set_position(x=200, y=-82, z=100, speed=speed, wait=True)
swift.set_position(x=150, y=47, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=71, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-45, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-73, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-73, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-85, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=134, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-73, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-30, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-28, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-44, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-69, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=103, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=53, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-28, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=112, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=103, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=78, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=87, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-5, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-39, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-112, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-80, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=104, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=98, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=81, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-146, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-142, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=37, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-95, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=136, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-77, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=107, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=6, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-27, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-61, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=20, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-35, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-30, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=141, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-24, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=46, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=33, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-34, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=107, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-54, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=32, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=61, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-115, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=8, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=86, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-115, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-60, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=105, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-28, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-86, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=23, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=93, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=4, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-118, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=53, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-61, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=122, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-86, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=110, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=13, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-127, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=15, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=13, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=62, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-41, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-91, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-141, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-20, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=71, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-53, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-29, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=121, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=128, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=12, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-97, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-56, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-47, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-23, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-63, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-30, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=136, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-1, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-89, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=43, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-26, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-110, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=9, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-79, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=66, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-43, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=72, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-26, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=143, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-109, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=40, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=120, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=88, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=97, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=91, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=110, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-24, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-65, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-90, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-94, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-84, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=60, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=107, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-5, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=45, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=91, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-98, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-127, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-18, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-16, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=97, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=131, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=121, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-11, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=53, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=76, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-64, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-24, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=41, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-132, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=134, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-55, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-31, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=34, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-49, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=39, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=56, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-41, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=105, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=8, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=103, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=104, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=85, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=135, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=109, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-27, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=111, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-8, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=5, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=140, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=121, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-16, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-112, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=127, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-69, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-67, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=142, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=63, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=88, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=49, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=69, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=5, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-33, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=42, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=149, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-68, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-85, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-55, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=48, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=104, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-27, z=30, speed=speed, wait=True)



print('Ending')
swift.reset(wait=True, speed=speed)
swift.set_digital_output(pin=49, value=0) # green led
swift.flush_cmd()
time.sleep(5)
swift.disconnect()
print('Finished')