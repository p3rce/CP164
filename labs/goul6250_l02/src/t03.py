"""
------------------------------------------------------------------------
[Lab 2, Task 3]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-23"
------------------------------------------------------------------------
"""

from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

stack = Stack()

source = ["top", "bottom"]

array_to_stack(stack, source)

target = []

stack_to_array(stack, target)

print(target)