"""
------------------------------------------------------------------------
[Lab 2, Task 2]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-23"
------------------------------------------------------------------------
"""

from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()

source = ["top", "bottom"]

array_to_stack(stack, source)

while not stack.is_empty():
    value = stack.pop()
    print(value)