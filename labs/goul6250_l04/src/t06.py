"""
------------------------------------------------------------------------
[Lab 4, Task 6]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-02-05"
------------------------------------------------------------------------
"""

from List_array import List
from utilities import array_to_list, list_to_array

llist = List()

source = [1, 2, 3, 4, 5]

array_to_list(llist, source)

print("Printing LList: ")
for value in llist:
    print(value)

list_to_array(llist, source)

print()
print("Printing List: ")
for value in source:
    print(value)