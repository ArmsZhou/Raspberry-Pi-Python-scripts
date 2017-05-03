#!usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 定义信号接口gpio口
INT1 = 11
INT2 = 12
INT3 = 13
INT4 = 15

signal_A = GPIO.HIGH
signal_B = GPIO.LOW


class Car(object):
    """docstring for Car"""

    def __init__(self):
        super(Car, self).__init__()
        # 设置gpio口的模式
        GPIO.setmode(GPIO.BOARD)
        # 设置gpio口为输出
        GPIO.setup(INT1, GPIO.OUT)
        GPIO.setup(INT2, GPIO.OUT)
        GPIO.setup(INT3, GPIO.OUT)
        GPIO.setup(INT4, GPIO.OUT)

    # 前进
    def forward(self):
        time.sleep(1)
        GPIO.output(INT1, signal_A)
        GPIO.output(INT2, signal_B)
        GPIO.output(INT3, signal_A)
        GPIO.output(INT4, signal_B)

    # 后退
    def backward(self):
        time.sleep(1)
        GPIO.output(INT1, signal_B)
        GPIO.output(INT2, signal_A)
        GPIO.output(INT3, signal_B)
        GPIO.output(INT4, signal_A)

    # 左转弯
    def left(self):
        time.sleep(1)
        GPIO.output(INT1, signal_A)
        GPIO.output(INT2, signal_B)
        GPIO.output(INT3, False)
        GPIO.output(INT4, False)
        self.stop()

    # 右转弯
    def right(self):
        time.sleep(1)
        GPIO.output(INT1, False)
        GPIO.output(INT2, False)
        GPIO.output(INT3, signal_A)
        GPIO.output(INT4, signal_B)
        self.stop()

    # 原地转圈
    def circle(self):
        time.sleep(1)
        GPIO.output(INT1, signal_A)
        GPIO.output(INT2, signal_B)
        GPIO.output(INT3, False)
        GPIO.output(INT4, False)

    # 停止
    def stop(self):
        time.sleep(1)
        GPIO.output(INT1, False)
        GPIO.output(INT2, False)
        GPIO.output(INT3, False)
        GPIO.output(INT4, False)
