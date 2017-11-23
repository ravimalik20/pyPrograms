#! /usr/bin/python3

class ShortInputException(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	val = input('Enter something:')

	if len(val) <= 10:
		raise ShortInputException(len(val), 10)
except EOFError:
	print ("EOF Encountered")
except KeyboardInterrupt:
	print ("Operation canceled.")
except ShortInputException as ex:
	print ("Input length: {} , expected length greater than: {}".format(
		ex.length, ex.atleast))
else:
	print ("Input received: {}".format(val))
