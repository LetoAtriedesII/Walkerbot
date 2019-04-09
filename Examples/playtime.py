#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFactory, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

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

'''
swift.reset(wait=True, speed=100000)
swift.set_position(x=200, speed=100000)
swift.set_position(y=100)
swift.set_position(z=100)
swift.flush_cmd(wait_stop=True)
'''
'''
swift.set_polar(stretch=150, speed=100000)
swift.set_polar(rotation=0)
swift.set_polar(height=80)
print(swift.set_polar(stretch=150, rotation=0, height=80, wait=True))
swift.flush_cmd()
'''
'''
swift.set_polar(stretch=150, rotation=90, height=150, speed=100000, wait=True)
print(swift.set_polar(stretch=150, rotation=90, height=150, wait=True))

swift.set_polar(stretch=300, rotation=90, height=30, speed=100000, wait=True)
print(swift.set_polar(stretch=300, rotation=90, height=30, wait=True))
'''
speed = 100
swift.reset(wait=True, speed=speed)

swift.set_position(x=150, y=150, z=30, speed=speed, wait=True)
print('Position 1 reached')
swift.set_position(x=200, y=-150, z=30, speed=speed, wait=True)
print('Position 2 reached')
swift.set_position(x=250, y=0, z=150, speed=speed, wait=True)
print('Position 3 reached')
swift.set_position(x=150, y=100, z=30, speed=speed, wait=True)
print('Position 4 reached')

print('begin')
swift.set_position(x=200, y=-21, z=100, speed=speed, wait=True)
swift.set_position(x=200, y=-7, z=100, speed=speed, wait=True)
swift.set_position(x=200, y=-54, z=100, speed=speed, wait=True)
swift.set_position(x=200, y=-72, z=100, speed=speed, wait=True)
swift.set_position(x=200, y=150, z=100, speed=speed, wait=True)
swift.set_position(x=150, y=24, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=81, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-75, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-149, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-122, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=-15, z=30, speed=speed, wait=True)
swift.set_position(x=150, y=0, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=150, z=150, speed=speed, wait=True)
swift.set_position(x=150, y=-150, z=30, speed=speed, wait=True)
swift.set_position(x=300, y=77, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-41, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-150, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-27, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=-17, z=150, speed=speed, wait=True)
swift.set_position(x=300, y=1, z=150, speed=speed, wait=True)

'''
swift.set_polar(stretch=150, rotation=0, height=150, speed=speed, wait=True)
swift.set_polar(stretch=300, rotation=180, height=30, speed=speed, wait=True)
'''

swift.reset(wait=True, speed=speed)
swift.flush_cmd()
time.sleep(5)
swift.disconnect()
print('End')