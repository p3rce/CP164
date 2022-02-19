"""
------------------------------------------------------------------------
[Lab 4, Task 7]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-02-05"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods
from utilities import list_test

file = open("food.txt", "rt")

source = read_foods(file)

file.close()

list_test(source)