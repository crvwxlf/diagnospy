#!/usr/bin/env python
# coding: utf-8
__author__ = " Kwalix"
__version__ = " 1.0"

import sys
import os
import socket
from pyfiglet import figlet_format
from termcolor2 import c


def menu():
    os.system('clear')
    print(c(figlet_format("Diagnospy")).red)
    print(c('Author :').white.on_blue + c(__author__).white)
    print(c('Versions:').white.on_red + __version__)


def main():
    print(c('\n1: Hardware Information').yellow)
    print(c('\n2: Network info').yellow)
    print(c('\n0: Quit').yellow)

    try:
        opt = input(c('\nChoose mode >>> ').cyan)
        opt = int(opt)
    except (NameError, SyntaxError):
        print(c('\nBad option').red)
        main()

    if opt == 0:
        print(c('\nExiting program...').red)
        sys.exit(0)
    elif opt == 1:
        print(c('\nHostname : ').yellow + os.popen('uname -n').read())
        print(c('\nPlatform architecture : ').yellow + os.popen("uname -m").read())
        print(c('\nOS Name : ').yellow + os.popen('uname -s').read())
        print(c('\nOS Version : ').yellow + os.popen('uname -v').read())
    elif opt == 2:
        print(c('\nInternal IP : ').yellow + os.popen('hostname -I').read())
        print(c('\nhostname IP :').yellow + socket.gethostbyname(socket.gethostname()))
        print(c('\nExternal IP : ').yellow + c('Coming soon...').red.blink)
    else:
        print(c('\nYou did not choose an option :(').red)
        main()

    while opt != 0:
        main()


menu()
try:
    main()
except KeyboardInterrupt:
    print(c('\nExiting program...\n').red)
    sys.exit(0)
