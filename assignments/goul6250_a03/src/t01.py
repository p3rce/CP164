"""
------------------------------------------------------------------------
[Task 1, Assignment 3]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-27"
------------------------------------------------------------------------
"""


from functions import stack_combine
from utilities import array_to_stack
from Stack_array import Stack

source1 = Stack() #Init a new stack
source2 = Stack() #Init a new stack

array_to_stack(source1, [5,8,12,8])
array_to_stack(source2, [3,6,1,7,9,14])


target = stack_combine(source1, source2)

while not target.is_empty():
    value = target.pop()
    print(value)