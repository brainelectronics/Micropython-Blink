#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Boot script

Do initial stuff here, similar to the setup() function on Arduino
"""

import esp
import gc
from machine import Pin


# disable ESP os debug output
esp.osdebug(None)

# set pin D4 as output (blue LED)
led_pin = Pin(4, Pin.OUT)

gc.collect()
