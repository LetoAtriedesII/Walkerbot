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

swift.reset(wait=True, speed=250)

swift.set_polar(stretch=150, speed=250)
swift.set_polar(rotation=0, speed=250) 
swift.set_polar(height=100, speed=250)
swift.flush_cmd(wait_stop=True)

swift.set_polar(stretch=200, speed=250)
swift.set_polar(rotation=90, speed=250)
swift.set_polar(height=50, speed=250)
swift.flush_cmd(wait_stop=True)

swift.set_polar(stretch=300, speed=250)
swift.set_polar(rotation=180, speed=250)
swift.set_polar(height=150, speed=250)
swift.flush_cmd(wait_stop=True)

swift.reset(wait=True, speed=100)
swift.flush_cmd()
time.sleep(5)
swift.disconnect()
