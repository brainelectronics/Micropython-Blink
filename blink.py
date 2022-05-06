#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Blink helper module

Toggle pin on and off
"""

import time


def flash_led(pin, amount, on_time=0.5, off_time=0.5):
    """
    Flash onboard LED at given pin

    :param      pin:       The pin connected to the LED
    :type       pin:       int
    :param      amount:    The amount the LED flashes
    :type       amount:    int
    :param      on_time:   On time of the LED
    :type       on_time:   float
    :param      off_time:  Off time of the LED
    :type       off_time:  float
    """
    for x in range(1, amount + 1):
        pin.value(1)
        time.sleep(on_time)
        pin.value(0)
        time.sleep(off_time)
