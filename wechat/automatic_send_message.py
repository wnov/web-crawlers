# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from wxpy import *
from requests import get
from requests import post
from platform import system
from os import chdir
from random import choice
from threading import Thread
import configparser
import time
import itchat


def send_message():
    pass


def main():
    pass


if __name__ == '__main__':
    itchat.login()

    # 启动微信机器人，自动根据操作系统执行不同的指令
    # windows系统或macOS Sierra系统使用bot = Bot()
    # linux系统或macOS Terminal系统使用bot = Bot(console_qr=2)

    # if ('Windows' in system()):
    #     # Windows
    #     bot = Bot()
    # elif ('Darwin' in system()):
    #     # MacOSX
    #     bot = Bot()
    # elif ('Linux' in system()):
    #     # Linux
    #     bot = Bot(console_qr=2, cache_path=True)
    # else:
    #     # 自行确定
    #     print("无法识别你的操作系统类型，请自己设置")

    print('Login successfully!')
