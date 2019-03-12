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

swift.set_polar(stretch=150, speed=100000)
swift.set_polar(rotation=90)
swift.set_polar(height=120)
print(swift.set_polar(stretch=150, rotation=90, height=120, wait=True))

swift.disconnect()
