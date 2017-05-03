#!usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Raspberry(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(Raspberry, self).__init__()

	def msg_handler(self, args):
		arg_list = args.split(" ")  # 参数以空格为分割符
		res = "Hi, i'm Pi."
		return res

