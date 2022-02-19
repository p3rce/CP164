"""
------------------------------------------------------------------------
[Assignment 2, Task 5]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-22"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods, food_table, food_search

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

result = food_search(foods, 11, 0, False)

food_table(result)