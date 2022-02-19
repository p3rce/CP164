"""
------------------------------------------------------------------------
[Lab 2, Task 1]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-23"
------------------------------------------------------------------------
"""

from Stack_array import Stack

stack = Stack()

if stack.is_empty():
    print("Stack is empty")
else:
    print("Stack is not empty")

stack.push(1)

value = stack.pop()

print(f"{value} is no longer in the stack")

stack.push("bottom")

stack.push("top")

print(stack.peek())