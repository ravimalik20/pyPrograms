#! /usr/bin/python3

import sys

class ArgsLenException(Exception):
	pass

try:
	argc = len(sys.argv)
	argv = sys.argv

	if argc == 1:
		raise ArgsLenException

	print("Number of command line args: {}".format(argc))
	print("List of command line args: {}".format(argv))

except ArgsLenException:
	sys.stderr.write("No extra command line arguments provided.\n")

sys.exit()
