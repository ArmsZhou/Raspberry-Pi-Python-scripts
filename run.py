#!usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
from PiMain import Raspberry

pi = Raspberry()


def lc():
    help_msg = u"请回复 help 获取帮助信息"
    itchat.send(help_msg, 'filehelper')


@itchat.msg_register(itchat.content.TEXT)
def pi_main(msg):
    if msg['ToUserName'] != 'filehelper':
        return
    text = msg['Text']
    res = pi.msg_handler(text)
    itchat.send(res, 'filehelper')


itchat.auto_login(hotReload=True, enableCmdQR=2, loginCallback=lc)
itchat.run(debug=True)
