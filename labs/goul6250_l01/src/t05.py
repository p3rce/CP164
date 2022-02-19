"""
------------------------------------------------------------------------
[Lab 1, Task 5]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

for food in foods:
    print(food, end="\n\n")