import sys
from math import sqrt
import dummy_module

# basically done to prevent execution of statements on module import
if __name__ == "__main__":
	print("Command line args: ", end = "")

	for i in sys.argv:
		print(i, end = " ")
	print("")

	print("Python path is:{0}".format(sys.path))

	print("sqrt({0}) is: {1}".format(1234, sqrt(1234)))

	dummy_module.printHello()
