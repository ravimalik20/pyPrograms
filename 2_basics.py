#! /usr/bin/python3

num_int = 1
num_long = 100000000000000000000000000000000000000000000000000000000000000009

num_float = 20.45
num_float2 = 20.45e10

# Strings are immutable.
string = "This is a string."
string2 = 'This is also a string.'
string_multiline = '''
This is
a multiline
string.
'''

print("Num_int: {0}\nNum_long: {1}\nNum_float: {2:.3f}\nNum_float2: {3}".format(
	num_int, num_long, num_float, num_float2))

print("String1: {}\nString2: {}\nMultiline String: {}".format(string, string2,
	string_multiline))

# Format string with 8 underscores and text within those underscores
print("{0:_^8}".format("ravi"))

print("This is {name}".format(name="Python!"))

print("Written by ", end='')
print("Ravi Malik")

# Raw String. Does not process escape sequences.
print(r"This is a raw '\/\\n\b\a' string")
