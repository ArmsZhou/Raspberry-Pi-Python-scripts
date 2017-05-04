#!usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


class DistanceDetector(object):
    """docstring for DistanceDetector"""

    def __init__(self, trig, echo, flag):
        super(DistanceDetector, self).__init__()
        self.TRIG = trig
        self.ECHO = echo
        self.start = 0
        self.stop = 0
        self.distance = -1
        self.flag = flag
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def start(self):
        try:
            while True:
                GPIO.output(self.TRIG, 0)
                time.sleep(0.01)

                GPIO.output(self.TRIG, 1)
                time.sleep(0.00001)
                GPIO.output(self.TRIG, 0)
                self.start = time.time()

                while GPIO.input(self.ECHO) == 0:
                    self.start = time.time()

                while GPIO.input(self.ECHO) == 1:
                    self.stop = time.time()

                self.distance = (self.stop - self.start) * \
                    34000 / 2  # 声波的速度是340m/s
                print u'%s 距离障碍物 %s cm' % (self.flag, self.distance)

        except Exception as e:
            raise e

    def tooclose(self):
        return self.distance <= 10
