import sys
import time

filename = "15_try_finally.py"
f = None

try:
	f = open(filename)

	line = f.readline()
	while len(line) > 0:
		print(line, end = '')
		line = f.readline()
except IOError:
	print ("Could not find file {}".format(filename))
finally:
	if f:
		f.close()
		print ("###### cleanup complete. #######")

# same as above. Will close the file automatically
with open(filename) as fl:
	for line in fl:
		print(line, end = '')
