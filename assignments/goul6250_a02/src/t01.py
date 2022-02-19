"""
------------------------------------------------------------------------
[Assignment 2, Task 1]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-22"
------------------------------------------------------------------------
"""

from Food import Food
from Food_utilities import read_foods, by_origin

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

origin = int(input(f"Enter a origin as an int\n{Food.origins()}: "))

origins = by_origin(foods, origin)

for food in origins:
    print(food, end="\n\n")