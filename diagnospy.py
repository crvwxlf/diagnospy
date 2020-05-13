#!/usr/bin/env python
# coding: utf-8
__author__ = " Kwalix"
__version__ = " In developement..."

import sys
import os
from pyfiglet import figlet_format
from termcolor2 import c

print(c(figlet_format("Diagnospy")).red)
print(c('Author :').white.on_blue + c(__author__).white)
print(c('Versions:').white.on_red + __version__)
