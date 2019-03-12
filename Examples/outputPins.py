#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFactory, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

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
if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
    swift.set_speed_factor(0.0005)

swift.set_mode(0)

'''
swift.reset(wait=True, speed=100000)
swift.set_position(x=200, speed=100000)
swift.set_position(y=100)
swift.set_position(z=100)
swift.flush_cmd(wait_stop=True)
'''

swift.set_polar(stretch=150, speed=100000)
swift.set_polar(rotation=90)
swift.set_polar(height=80)
print(swift.set_polar(stretch=150, rotation=90, height=80, wait=True))
swift.flush_cmd()

#set_digital_output(pin=None, value=None, wait=True, timeout=None, callback=None)
swift.set_digital_output(pin=0, value=1)
swift.set_digital_output(pin=1, value=1)
swift.set_digital_output(pin=2, value=1)
swift.set_digital_output(pin=3, value=1)
swift.set_digital_output(pin=4, value=1)
swift.set_digital_output(pin=5, value=1)
swift.set_digital_output(pin=6, value=1)
swift.set_digital_output(pin=7, value=1)
swift.set_digital_output(pin=8, value=1)
swift.set_digital_output(pin=9, value=1)
swift.set_digital_output(pin=10, value=1)
swift.set_digital_output(pin=11, value=1)
swift.set_digital_output(pin=12, value=1)
swift.set_digital_output(pin=13, value=1)
swift.set_digital_output(pin=14, value=1)
swift.set_digital_output(pin=15, value=1)
swift.set_digital_output(pin=16, value=1)
swift.set_digital_output(pin=17, value=1)
swift.set_digital_output(pin=18, value=1)
swift.set_digital_output(pin=19, value=1)
swift.set_digital_output(pin=20, value=1)
swift.set_digital_output(pin=21, value=1)
swift.set_digital_output(pin=22, value=1)
swift.set_digital_output(pin=23, value=1)
swift.set_digital_output(pin=24, value=1)
swift.set_digital_output(pin=25, value=1)
swift.set_digital_output(pin=26, value=1)
swift.set_digital_output(pin=27, value=1)
swift.set_digital_output(pin=28, value=1)
swift.set_digital_output(pin=29, value=1)
swift.set_digital_output(pin=30, value=1)
swift.flush_cmd()

swift.set_polar(stretch=150, speed=100000)
swift.set_polar(rotation=90)
swift.set_polar(height=120)
print(swift.set_polar(stretch=150, rotation=90, height=120, wait=True))

swift.disconnect()
