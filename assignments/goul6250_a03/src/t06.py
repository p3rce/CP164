"""
------------------------------------------------------------------------
[Assignment 3, Task 6]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-28"
------------------------------------------------------------------------
"""

from functions import reroute

opstring = input("Enter opstring: ")

values_in = [1, 2, 3, 4, 5, 6]

values_out = reroute(opstring, values_in)

print(values_out)