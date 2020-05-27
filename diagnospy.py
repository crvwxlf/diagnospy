#!/usr/bin/env python3
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


def menu():
    os.system("clear")
    print(c(figlet_format("Diagnospy")).red)
    print(c("Author :").white.on_blue + c(__author__).white)
    print(c("Versions:").white.on_red + __version__)


def main():
    while True:
        # All Vars for main function
        host_n = os.popen("uname -n").read()
        arch = os.popen("uname -m").read()
        os_name = os.popen("uname -s").read()
        os_ver = os.popen("uname -v").read()
        iip = os.popen("hostname -I").read()
        hip = socket.gethostbyname(socket.gethostname())
        cwd = os.getcwd()

        # Choice menu
        print(c("\n1: Hardware Information").yellow)
        print(c("\n2: Network info").yellow)
        print(c("\n3: Create and save diagnostic report in a txt file").yellow)
        print(c("\n99: Quit").yellow)

        opt = input(c("\nChoose mode >>> ").cyan)

        if opt == "99":
            print(c("\nExiting program...").green)
            sys.exit(0)
        elif opt == "1":
            print(c("\nHostname : ").yellow + host_n)
            print(c("\nPlatform architecture : ").yellow + arch)
            print(c("\nOS Name : ").yellow + os_name)
            print(c("\nOS Version : ").yellow + os_ver)
        elif opt == "2":
            print(c("\nInternal IP : ").yellow + iip)
            print(c("\nhostname IP :").yellow + hip)
            print(c("\nExternal IP : ").yellow + c("Coming soon...").red.blink)
        elif opt == "3":
            file_name = datetime.datetime.date(datetime.datetime.now())  # Generate actual date
            file_name = str(file_name)  # Converting date to string format
            file_name = file_name + ".txt"  # add .txt suffix to file name
            with open(file_name, "w+") as file:  # Creating file and write all data and close it
                file.write(
                    "Hostname : "
                    + host_n
                    + "\nArch : "
                    + arch
                    + "\nOS Name : "
                    + os_name
                    + "\nOS Version : "
                    + os_ver
                    + "\nInternal IP : "
                    + iip
                    + "\nHostname IP "
                    + hip
                    + "\nExternal IP : N\\A"
                )
            # Returning path of report file
            print(c("\nyour file as been saved in : ").yellow + cwd + "/" + file_name)
            while True:
                a_quit = input("\nExit Diagnospy ? [y/n] : ")

                if a_quit == "y":
                    print(c("\nGood bye").green)
                    sys.exit(0)
                elif a_quit == "n":
                    print(c("\nReturning to main menu").green)
                    time.sleep(0.5)
                    os.system("clear")
                    menu()
                    main()
                else:
                    continue
        else:
            continue


# Launching menu and main function
if __name__ == '__main__':

    menu()
    try:
        main()
    except KeyboardInterrupt:
        print(c("\nExiting program...\n").red)
        sys.exit(0)
