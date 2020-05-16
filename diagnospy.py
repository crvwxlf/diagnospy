#!/usr/bin/env python
# coding: utf-8
__author__ = " Kwalix"
__version__ = " 1.0"

import sys
import os
import socket
import time
import datetime
from pyfiglet import figlet_format
from termcolor2 import c

# Global vars

global host_n, arch, os_name, os_ver, iip, hip, eip, cwd
host_n = os.popen('uname -n').read()
arch = os.popen("uname -m").read()
os_name = os.popen('uname -s').read()
os_ver = os.popen('uname -v').read()
iip = os.popen('hostname -I').read()
hip = socket.gethostbyname(socket.gethostname())
cwd = os.getcwd()


def menu():
    os.system('clear')
    print(c(figlet_format("Diagnospy")).red)
    print(c('Author :').white.on_blue + c(__author__).white)
    print(c('Versions:').white.on_red + __version__)


def main():
    # Choice menu
    print(c('\n1: Hardware Information').yellow)
    print(c('\n2: Network info').yellow)
    print(c('\n3: Create and save diagnostic report in a txt file').yellow)
    print(c('\n99: Quit').yellow)

    try:
        opt = input(c('\nChoose mode >>> ').cyan)
        opt = int(opt)
    except (NameError, SyntaxError):
        print(c('\nBad option').red)
        time.sleep(0.5)
        os.system('clear')
        menu()
        main()

    if opt == 99:
        print(c('\nExiting program...').red)
        sys.exit(0)
    elif opt == 1:
        print(c('\nHostname : ').yellow + host_n)
        print(c('\nPlatform architecture : ').yellow + arch)
        print(c('\nOS Name : ').yellow + os_name)
        print(c('\nOS Version : ').yellow + os_ver)
    elif opt == 2:
        print(c('\nInternal IP : ').yellow + iip)
        print(c('\nhostname IP :').yellow + hip)
        print(c('\nExternal IP : ').yellow + c('Coming soon...').red.blink)
    elif opt == 3:
        save_report()
        try:
            askquit = input(c('\nEnter 1 for exit\nEnter 0 or Enter for continue\nExit Diagnospy ? : ').cyan)
            askquit = int(askquit)
        except (SyntaxError, ValueError):
            print(c('\nReturning to main menu').green)
            time.sleep(0.5)
            os.system('clear')
            menu()
            main()
        except NameError:
            askquit

        if askquit == 1:
            print(c('\nGood bye').green)
            sys.exit(0)
        else:
            print(c('\nReturning to main menu').green)
            time.sleep(0.5)
            os.system('clear')
            menu()
            main()
    else:
        print(c('\nYou did not choose an option :(').red)
        time.sleep(0.5)
        os.system('clear')
        menu()
        main()

    while opt != 99:
        main()


def save_report():
    file_name = datetime.datetime.date(datetime.datetime.now())
    file_name = str(file_name)
    file_name = file_name + '.txt'
    file = open(file_name, 'w+')
    file.write(
        'Hostname : ' + host_n + '\nArch : ' + arch + '\nOS Name : ' + os_name + '\nOS Version : ' + os_ver + '\nInternal IP : ' + iip + '\nHostname IP ' + hip + '\nExternal IP : N\A')
    file.close()
    print(c('\nyour file as been saved in : ').yellow + cwd + '/' + file_name)


# Launching menu and main function
menu()
try:
    main()
except KeyboardInterrupt:
    print(c('\nExiting program...\n').red)
    sys.exit(0)
