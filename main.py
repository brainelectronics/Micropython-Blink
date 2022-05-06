#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, similar to the loop() function on Arduino
"""

from blink import flash_led


def loop():
    # loop forever
    while True:
        # flash LED 3 times, then sleep for 3 seconds
        flash_led(led_pin, 3)
        time.sleep(3)


# MicroPython calls every function inside this file
loop()
