"""
------------------------------------------------------------------------
[Lab 3, Task 1]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-29"
------------------------------------------------------------------------
"""

from Queue_array import Queue

queue = Queue()

value = input("Enter a value: ")

queue.insert(value)

print(len(queue))