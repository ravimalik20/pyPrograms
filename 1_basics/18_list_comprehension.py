#! /usr/bin/python3

# TODO: Nested list comprehension.

def square(l):
	return list(map(lambda x:x**2, l))

# A list comprehension consists of brackets containing an expression followed
# by a for clause, then zero or more for or if clauses. The result will be a
# new list resulting from evaluating the expression in the context of the for
# and if clauses which follow it.
def square2(l):
	return [x**2 for x in l]

l = range(10)

print(square(l))
print(square2(l))

# example taken from python docs. Subsequent for statements after the first one
# will be nested.
l = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

print (l)
