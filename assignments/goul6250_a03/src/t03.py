"""
------------------------------------------------------------------------
[Assignment 3, Task 3]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-28"
------------------------------------------------------------------------
"""

from Stack_array import Stack
from functions import stack_reverse
from utilities import array_to_stack

source1 = Stack()

array_to_stack(source1, [5, 8, 12, 8])

stack_reverse(source1)

while not source1.is_empty():
    value = source1.pop()
    print(value)