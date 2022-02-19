"""
------------------------------------------------------------------------
[Lab 3, Task 5]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-29"
------------------------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

value = int(input("Enter a number: "))

pq.insert(value)

print(pq.remove())