'''
Author: Adam Novak

Description: This code emulates WALKING motion. The data points were gathered by using the Grace Industries PASS sensor.

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

swift.set_position(x=200, y=23, z=100, speed=speed, wait=True)
swift.set_position(x=200, y=136, z=100, speed=speed, wait=True)
swift.set_position(x=200, y=142, z=100, speed=speed, wait=True)
swift.set_position(x=200, y=150, z=100, speed=speed, wait=True)
swift.set_position(x=150, y=127, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=145, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=142, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-93, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-8, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-52, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-102, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=32, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-110, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=110, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-48, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-58, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-120, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-138, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-39, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=7, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-80, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-82, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-13, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-29, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=100, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-24, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=74, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-103, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=67, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=50, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=145, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-38, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-139, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=131, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=62, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-78, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-2, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=132, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=84, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=46, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=102, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-101, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=44, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-46, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-124, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-136, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-91, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-148, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-40, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=97, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-72, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-68, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=78, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=42, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-13, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-27, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-117, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-62, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=17, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=92, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=19, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-81, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-133, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=0, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=119, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=91, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=125, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=51, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=81, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=34, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=13, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-35, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=1, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-81, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=5, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=58, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-64, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-148, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=99, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-95, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-71, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-57, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-121, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=8, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=46, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=97, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=104, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=62, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=69, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=15, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-9, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-51, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-20, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-33, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=18, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-93, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-70, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=26, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=4, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-93, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=85, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=35, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-54, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-96, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=16, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-7, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-139, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-14, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-119, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-130, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=70, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=44, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=33, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-65, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-98, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-72, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-115, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-126, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=11, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=105, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-51, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-107, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-101, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-27, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=93, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=57, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=98, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=119, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-69, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-103, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-71, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=55, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=8, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=7, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=92, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=89, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-132, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-85, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-101, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-29, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=50, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-118, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-41, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=106, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-1, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-67, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-69, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=20, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-45, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-58, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-71, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=125, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=68, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=70, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-147, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-83, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=134, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=17, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-107, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-9, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-102, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-89, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=72, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=148, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-39, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-6, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-60, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=35, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-91, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-103, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=147, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=19, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=98, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=147, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=3, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-42, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=56, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=43, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=100, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=3, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-56, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-19, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=13, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-6, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=10, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-18, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-24, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-38, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-126, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-112, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=16, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=15, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=44, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)

print('Ending')
swift.reset(wait=True, speed=speed)
swift.set_digital_output(pin=49, value=0) # green led
swift.flush_cmd()
time.sleep(5)
swift.disconnect()
print('Finished')