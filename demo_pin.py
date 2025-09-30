
#! /usr/bin/env python3
# Author: KPawar
# Description: This script will simulate a high street bank ATM machine
"""
    Docstring:
"""

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    #will only execute is while loop becomes false
    print("too many attempts")
    print("your card has been retained, have a bad day!")

print("Done")

