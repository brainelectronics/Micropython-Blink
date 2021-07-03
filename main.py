#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
main script, do your stuff here, similar to the loop() function on Arduino
"""
import time
from machine import Pin


def flash_led(pin, amount):
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


if __name__ == '__main__':
    loop()
