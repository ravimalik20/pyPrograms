#! /usr/bin/python3

# Prepare dictionary from list l, with list element as key and it's square as
# value, only for odd numbers in list

l = range(45)
dict1 = {x:x**2 for x in l if x%2 == 0}
print(dict1)

# prepare dictionary from a list of tuples
l2 = [(x, x**3) for x in range(50) if x%5 == 0]
print(l2)
dict2 = dict(l2)
print(dict2)
