"""
------------------------------------------------------------------------
[Lab 3, Task 3]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-29"
------------------------------------------------------------------------
"""

from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test

queue = Queue()

source = [1, 2, 3]

array_to_queue(queue, source)

for _ in range(len(queue)):
    value = queue.remove()
    print(value)
    source.append(value)

array_to_queue(queue, source)

queue_to_array(queue, source)

print(source)

queue_test(source)