"""
------------------------------------------------------------------------
[Assignment 2, Task 4]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-22"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods, food_table

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

food_table(foods)