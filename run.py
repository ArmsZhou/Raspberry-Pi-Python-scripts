#!usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
from PiMain import Raspberry

pi = Raspberry()

@itchat.msg_register(itchat.content.TEXT)
def pi_main(msg):
	if msg['ToUserName'] != 'filehelper': return
	text = msg['Text']
	res = pi.msg_handler(text)
	itchat.send(res, 'filehelper')

itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run(debug=True)