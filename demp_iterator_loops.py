#! /usr/bin/env python3
# Author: KPawar
# Description: This script will demo how to iterate through a collection/sequence (str/tuple/list/dict/set) using an ITERATOR for loop.
"""
    Docstring:
"""
import sys

heroes = ['JFK', "M.Jackson", "Ozzie", "Malcolm X", "Pele", "Kobe", "Diana"]

# Iterate through the collection/list using an interator for loop

for name in heroes:
    print(name)


# Iterate through the collection/list and MODIFY the objects
# using an interator for loop and an index counter
idx = 0
for name in heroes:
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes =", heroes)

# Iterate through the collection/list and MODIFY the objects
# using an interator for loop and built-in enumerate() function
for idx, name in enumerate(heroes, start=0): #this will return a tuple
    print(name.upper(), end="\n")
    heroes[idx] = name.title()
print("Heroes =", heroes)

import sys
sys.exit("Goodbye") #explicit EXIT with return code (0=success, 1-225=error code)


