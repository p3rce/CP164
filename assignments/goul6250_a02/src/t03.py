"""
------------------------------------------------------------------------
[Assignment 2, Task 3]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-22"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods, calories_by_origin

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

avg = calories_by_origin(foods, 2)

print(f"Average Calories: {avg}")