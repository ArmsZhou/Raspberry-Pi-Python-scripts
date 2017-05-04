#!usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


class Led(object):
    """docstring for Led"""

    def __init__(self, gpio):
        super(Led, self).__init__()
        self.PIN_NO = gpio
        self.flashing = False
        GPIO.setup(self.PIN_NO, GPIO.OUT)

    def flashing(self):
        self.flashing = True
        while self.flashing:
            GPIO.output(self.PIN_NO, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.PIN_NO, GPIO.LOW)
            time.sleep(0.5)

    def light(self):
        self.flashing = False
        time.sleep(0.5)
        GPIO.output(self.PIN_NO, GPIO.HIGH)
