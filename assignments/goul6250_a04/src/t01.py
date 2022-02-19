"""
------------------------------------------------------------------------
[Assignment 4, Task 1]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-02-03"
------------------------------------------------------------------------
"""

from Queue_circular import Queue

queue = Queue(3)

print(len(queue))

print(queue.is_empty())

queue.insert(100)

print(len(queue))

value = queue.peek()

print(value)

removed = queue.remove()

print(removed)



queue.insert(100)
queue.insert(200)
queue.insert(300)
print(queue.is_full())