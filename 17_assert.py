#! /usr/bin/python3

shopping_list = ['spinach']

try:
	assert len(shopping_list) > 1
except AssertionError:
	print ("Assertion has failed.");
