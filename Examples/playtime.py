#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFactory, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

'''
stretch (mm)        : 150 -> 300
rotation (degrees)  :   0 -> 180 
height (mm)         :  30 -> 150 
speed (mm/s?)       :   0 -> 250
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

swift.reset(wait=True, speed=250)
speed = 100

swift.set_position(x=130, y=180, z=30, speed=speed, wait=True)
print('Position 1 reached')
swift.set_position(x=200, y=-180, z=30, speed=speed, wait=True)
print('Position 2 reached')
swift.set_position(x=250, y=0, z=150, speed=speed, wait=True)
print('Position 3 reached')
swift.set_position(x=150, y=100, z=30, speed=speed, wait=True)
print('Position 4 reached')

'''
swift.set_polar(stretch=150, rotation=0, height=150, speed=speed, wait=True)
swift.set_polar(stretch=300, rotation=180, height=30, speed=speed, wait=True)
'''

swift.reset(wait=True, speed=50)
swift.flush_cmd()
time.sleep(5)
swift.disconnect()