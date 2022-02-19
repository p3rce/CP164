"""
------------------------------------------------------------------------
[Assignment 3, Task 2]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-28"
------------------------------------------------------------------------
"""

from Stack_array import Stack
from utilities import array_to_stack

source1 = Stack()

source2 = Stack()

array_to_stack(source1, [5, 8, 12, 8])

array_to_stack(source2, [3, 6, 1, 7, 9, 14])

target = Stack()

target.combine(source1, source2)

while not target.is_empty():
    value = target.pop()
    print(value)