#!/usr/bin/env python
# coding: utf-8
__author__ = " Kwalix"
__version__ = " In developement..."

import sys
import os
import time
from pyfiglet import figlet_format
from termcolor2 import c


print(c(figlet_format("Diagnospy")).red)
print(c('Author :').white.on_blue + c(__author__).white)
print(c('Versions:').white.on_red + __version__)


def choice():
    print(c('\n1: Hardware Information').yellow)
    print(c('\n00: Quit').yellow)
    opt = input(c('\nChoose mode >>> ').cyan)
    opt = int(opt)
    if opt == 00:
        print(c('Exiting program...').red)
        sys.exit(0)
    elif opt == 1:
        print(c('\nHostname : ').yellow + os.popen('uname -n').read())
        print(c('Platform support : ').yellow + os.popen("uname -m").read())
    while opt != 00:
        os.system('clear')
        choice()

try:
    choice()
except (KeyboardInterrupt, SystemExit) as exit:
    print('\nKeyboardInterrupt Detected, press Ctrl+C one more time for exit now')
    time.sleep(2)