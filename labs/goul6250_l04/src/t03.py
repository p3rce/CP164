"""
------------------------------------------------------------------------
[Lab 4, Task 3]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-02-05"
------------------------------------------------------------------------
"""

from List_array import List

list1 = List()

list1.append(100)

print(len(list1))

list1.insert(0, 200)

print(len(list1))

remove = list1.remove(200)

print(remove)