#! /usr/bin/env python3
# Author: KPawar
# Description: This script will demo HOWTO check which plaform your program is running on...
"""
    Docstring:
"""

import sys
import os

my_home = None

if sys.platform == "win32":
    my_home = os.environ['HOMEPATH']
elif sys.platform == "darwin" or sys.platform == "linux":
    my_home = os.environ['HOME']
else:
    print("unknown platform")

print("Home is", my_home)