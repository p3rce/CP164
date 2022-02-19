"""
------------------------------------------------------------------------
[Lab 3, Task 2]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-29"
------------------------------------------------------------------------
"""

from Queue_array import Queue

queue = Queue()

insert_value = input("Enter a value: ")

queue.insert(insert_value)

print(queue.peek())

value = queue.remove()

print(value)