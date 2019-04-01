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

"""
api test: move
"""

swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})

swift.waiting_ready(timeout=3)

device_info = swift.get_device_info()
print(device_info)
firmware_version = device_info['firmware_version']

swift.set_mode(0)

swift.reset(wait=True, speed=250)
swift.set_position(x=300, speed=250)
swift.set_position(y=200)
swift.set_position(z=100)
swift.flush_cmd(wait_stop=True)
swift.set_polar(stretch=300, rotation=0, height=100, wait=True)
swift.set_polar(stretch=300, speed=250)
swift.set_polar(rotation=0)
swift.set_polar(height=100)
print()
swift.flush_cmd()

time.sleep(3)

swift.disconnect()