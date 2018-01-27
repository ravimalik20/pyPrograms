#! /usr/bin/python3

import numpy as np

arr = np.array([87, 2, 28, 8, 39, 56, 51, 11, 6, 95]);

print (arr)

print (arr.max())
print (arr.min())
print (arr.mean())

# Similar to partition subroutine in quicksort
print (arr.partition(5))
print (arr)

# Slicing does not create a copy, makes reference
arr2 = arr[2:5]
print (arr2)
arr[:3] = 0
print (arr2, arr)
