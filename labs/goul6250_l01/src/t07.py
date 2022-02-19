"""
------------------------------------------------------------------------
[Lab 1, Task 7]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods, get_vegetarian

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

veggies = get_vegetarian(foods)

for food in veggies:
    print(food, end="\n\n")