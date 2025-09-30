#! /usr/bin/env python3
# Author: KPawar
# Description: This script will demo HOWTO to repeat a block of commands a specific number of times using a counter loop.
"""
    Docstring:
"""

count = 0 # 1. Initialise counter
while count < 10: # 2.Test condition
    print(count)
    count += 1 # 2.Increment/Decrement counter


#Alternatively we could use a for loop plus the built-in range (start, stop, step) function
for num in range(0, 10, 1):
    print(num)