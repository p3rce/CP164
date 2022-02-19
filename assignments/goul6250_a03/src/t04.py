"""
------------------------------------------------------------------------
[Assignment 3, Task 4]
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

array_to_stack(source1, [5, 8, 12, 8])

source1.reverse()

while not source1.is_empty():
    value = source1.pop()
    print(value)