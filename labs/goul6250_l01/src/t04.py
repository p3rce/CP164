"""
------------------------------------------------------------------------
[Lab 1, Task 4]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""

from Food_utilities import read_food

to_read = input("Enter food details: ")
food = read_food(to_read)

print(food)