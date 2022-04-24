#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, similar to the loop() function on Arduino
"""

import time


def flash_led(pin, amount):
    """
    Flash onboard LED

    :param      pin:     The pin connected to the LED
    :type       pin:     int
    :param      amount:  The amount the LED flashes
    :type       amount:  int
    """
    for x in range(1, amount + 1):
        pin.value(1)
        time.sleep(0.05)
        pin.value(0)
        time.sleep(0.05)


def loop():
    # loop forever
    while True:
        flash_led(led_pin, 3)
        time.sleep(3)


# MicroPython calls every function inside this file
loop()
