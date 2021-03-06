"""
------------------------------------------------------------------------
[Assignment 4, Task 2]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-02-04"
------------------------------------------------------------------------
"""

from Queue_circular import Queue
from functions import queue_split_alt

source = Queue(3)

source.insert(1)

source.insert(2)

source.insert(3)

target1, target2 = queue_split_alt(source)


print("Printing Target 1...")
while len(target1) > 0:
    print(target1.remove())

print("Printing Target 2...")
while len(target2) > 0:
    print(target2.remove())