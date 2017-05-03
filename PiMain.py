#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
from car import Car


class Raspberry(object):
    """docstring for ClassName"""

    def __init__(self):
        super(Raspberry, self).__init__()
        self.help_msg = \
            u"你好，我是小Pi，回复对应字母开启我吧\n\n" \
            u"F: 前进\n" \
            u"B: 后退\n" \
            u"L: 左转弯\n" \
            u"R: 右转弯\n"\
            u"C: 原地转圈\n"\
            u"S: 停止\n"
        self.car = Car()

    def msg_handler(self, args):
        arg_list = args.split(" ")  # 参数以空格为分割符
        res = u"指令错误，回复 help 获取帮助"
        if len(arg_list) == 1:  # 如果接收参数个数为1
            arg = arg_list[0].strip()
            if arg == u'help':  # 帮助信息
                res = self.help_msg
            elif arg == u'F':
                self.car.forward()
                res = u"正在前进"
            elif arg == u'B':
                self.car.backward()
                res = u"正在后退"
            elif arg == u'L':
                self.car.left()
                res = u"正在左转弯"
            elif arg == u'R':
                self.car.right()
                res = u"正在右转弯"
            elif arg == u'C':
                self.car.circle()
                res = u"正在原地转圈"
            elif arg == u'S':
                self.car.stop()
                res = u"停止"

        return res
