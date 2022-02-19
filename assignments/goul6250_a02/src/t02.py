"""
------------------------------------------------------------------------
[Assignment 2, Task 2]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-22"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods, average_calories

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

avg = average_calories(foods)

print(f"Average Calories: {avg}")