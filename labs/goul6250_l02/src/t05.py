"""
------------------------------------------------------------------------
[Lab 2, Task 5]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-23"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods
from utilities import stack_test

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

stack_test(foods)