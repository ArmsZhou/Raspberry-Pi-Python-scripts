#!usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from led import Led
from distancedetector import DistanceDetector

# 定义信号接口gpio口
INT1 = 11
INT2 = 12
INT3 = 13
INT4 = 15

signal_A = GPIO.HIGH
signal_B = GPIO.LOW

# 感应器信号接口gpio口
FTRIG = 11
FECHO = 12

BTRIG = 13
BECHO = 14

# LED灯信号接口gpio口
FLED = 16
BLED = 17


class Car(object):
    """docstring for Car"""

    def __init__(self):
        super(Car, self).__init__()
        # 使用前先清理一遍GPIO
        GPIO.cleanup()
        # 设置gpio口的模式
        GPIO.setmode(GPIO.BOARD)
        # 设置gpio口为输出
        GPIO.setup(INT1, GPIO.OUT)
        GPIO.setup(INT2, GPIO.OUT)
        GPIO.setup(INT3, GPIO.OUT)
        GPIO.setup(INT4, GPIO.OUT)
        # 当前运行状态 -1 后退 0 静止 1 前进 2 原地转圈
        self.status = 0
        # 构造距离感应器实例和警报灯实例
        self.frontDetector = DistanceDetector(FTRIG, FECHO, u"Front")
        self.frontLed = Led(FLED)
        self.backDetector = DistanceDetector(BTRIG, BECHO, u"Back")
        self.backLed = Led(BLED)
        # 开启距离检测和警报灯
        self.frontDetector.start()
        self.frontLed.light()
        self.backDetector.start()
        self.backLed.light()
        while True:
            # 每隔 0.1s 检测前后距离
            time.sleep(0.1)
            if self.frontDetector.tooclose and self.backDetector.tooclose:
                self.stop()
                self.frontLed.flashing()
                self.backLed.flashing()
            elif self.frontDetector.tooclose:
                self.stop()
                self.frontLed.flashing()
                self.backLed.light()
            elif self.backDetector.tooclose:
                self.stop()
                self.frontLed.light()
                self.backLed.flashing()

    # 前进
    def forward(self):
        self.status = 1
        time.sleep(0.5)
        if self.status == 1:
            GPIO.output(INT1, signal_A)
            GPIO.output(INT2, signal_B)
            GPIO.output(INT3, signal_A)
            GPIO.output(INT4, signal_B)

    # 后退
    def backward(self):
        self.status = -1
        time.sleep(0.5)
        if self.status == -1:
            GPIO.output(INT1, signal_B)
            GPIO.output(INT2, signal_A)
            GPIO.output(INT3, signal_B)
            GPIO.output(INT4, signal_A)

    # 左转弯
    def left(self):
        time.sleep(0.5)
        GPIO.output(INT1, signal_A)
        GPIO.output(INT2, signal_B)
        GPIO.output(INT3, False)
        GPIO.output(INT4, False)
        self.stop()

    # 右转弯
    def right(self):
        time.sleep(0.5)
        GPIO.output(INT1, False)
        GPIO.output(INT2, False)
        GPIO.output(INT3, signal_A)
        GPIO.output(INT4, signal_B)
        self.stop()

    # 原地转圈
    def circle(self):
        self.status = 2
        time.sleep(0.5)
        if self.status == 2:
            GPIO.output(INT1, signal_A)
            GPIO.output(INT2, signal_B)
            GPIO.output(INT3, False)
            GPIO.output(INT4, False)

    # 停止
    def stop(self):
        self.status = 0
        time.sleep(0.5)
        GPIO.output(INT1, False)
        GPIO.output(INT2, False)
        GPIO.output(INT3, False)
        GPIO.output(INT4, False)
