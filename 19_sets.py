#! /usr/bin/python3

# Set is an unordered collection of data. Used basically for member testing and
# to remove duplicates. Mathematical operations supported like: union,
# intersection, difference and symmetric difference.

shopping_set = {'kale', 'spinach', 'kale', 'brocoli', 'halfnhalf', 'halfnhalf'}
print (shopping_set)

print ("spinach" in shopping_set)

# Can't use {} to init empty set. That's dictionary.
empty_set = set()

# Example taken from python docs.
a = set('abracadabra')
b = set('alacazam')

print("a: {}\nb: {}".format(a, b))

print ("Letters in a but not in b: {}".format(a - b))

print ("Letters in a or b or both: {}".format(a | b))

print ("Letters in both a and b: {}".format(a & b))

print ("Letters in a or b, but not both: {}".format(a ^ b))

# Set comprehensions.
set3 = {x for x in "abracadabra" if x not in "abc"}
print (set3)
