#!/usr/bin/env python
# coding: utf-8
__author__ = " Kwalix"
__version__ = " 1.0"

import sys
import os
from pyfiglet import figlet_format
from termcolor2 import c


def menu():
    os.system('clear')
    print(c(figlet_format("Diagnospy")).red)
    print(c('Author :').white.on_blue + c(__author__).white)
    print(c('Versions:').white.on_red + __version__)


def main():
    print(c('\n1: Hardware Information').yellow)
    print(c('\n0: Quit').yellow)

    opt = input(c('\nChoose mode >>> ').cyan)
    opt = int(opt)
    if opt == 0:
        print(c('\nExiting program...').red)
        sys.exit(0)
    elif opt == 1:
        print(c('\nHostname : ').yellow + os.popen('uname -n').read())
        print(c('Platform support : ').yellow + os.popen("uname -m").read())
    else:
        print('You are not choose option')
        main()

    while opt != 0:
        main()


try:
    menu()
    main()
except KeyboardInterrupt:
    print(c('\nExiting program...').red)
    sys.exit(0)
except (SyntaxError, NameError):
    print(c('\nBad option').red)
    main()
