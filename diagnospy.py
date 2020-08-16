#!/usr/bin/env python3
# coding: utf-8
__author__ = "Kwalix"
__version__ = "1.3.6"

import sys
import os
import platform
import socket
import distro
import time
import datetime
from requests import get


def menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("""
     ____  _                                         
    |  _ \(_) __ _  __ _ _ __   ___  ___ _ __  _   _ 
    | | | | |/ _` |/ _` | '_ \ / _ \/ __| '_ \| | | |
    | |_| | | (_| | (_| | | | | (_) \__ \ |_) | |_| |
    |____/|_|\__,_|\__, |_| |_|\___/|___/ .__/ \__, |
                   |___/                |_|    |___/ 
    By : {0} 
    Ver : {1}
    """.format(__author__, __version__))


def main():
    while True:
        # All Vars for main function
        host_n = platform.node()
        c_arch = platform.architecture()[0]
        os_name = sys.platform
        os_ver = distro.linux_distribution()[0]
        iipr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        eip = get('https://api.ipify.org').text

        try:
            iipr.connect(("8.8.8.8", 80))
        except OSError:
            iip = "Not available"
        else:
            iip = str(iipr.getsockname()[0])
        cwd = os.getcwd()

        # Choice menu
        print("\n1: Hardware Information")
        print("\n2: Network info")
        print("\n3: Create and save diagnostic report in a txt file")
        print("\n99: Quit")

        opt = input("\nChoose mode >>> ")

        if opt == "99":
            print("\nExiting program...")
            sys.exit(0)
        elif opt == "1":
            print("\nHostname : " + host_n)
            print("\nCore arch : " + c_arch)
            print("\nOS Name : " + os_name)
            print("\nOS Version : " + os_ver)
        elif opt == "2":
            print("\nInternal IP : " + iip)
            print("\nExternal IP : " + eip)
        elif opt == "3":
            file_name = datetime.datetime.date(datetime.datetime.now())  # Generate actual date
            file_name = str(file_name)  # Converting date to string format
            file_name = file_name + ".txt"  # add .txt suffix to file name
            with open(file_name, "w+") as file:  # Creating file and write all data and close it
                file.write(
                    "Hostname : %s \
                    \nCore arch : %s \
                    \nOS Name : %s \
                    \nOS Version : %s \
                    \nInternal IP : %s \
                    \nExternal IP : %s \n"
                    % (host_n, c_arch, os_name, os_ver, iip, eip)
                )
            # Returning path of report file
            print("\nyour file as been saved in : " + cwd + "/" + file_name)
            while True:
                a_quit = input("\nExit Diagnospy ? [y/n] : ")

                if a_quit == "y":
                    print("\nGood bye")
                    sys.exit(0)
                elif a_quit == "n":
                    print("\nReturning to main menu")
                    time.sleep(0.5)
                    os.system('clear' if os.name == 'posix' else 'cls')
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
        print("\nExiting program...\n")
        sys.exit(0)
