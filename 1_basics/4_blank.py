#! /usr/bin/python3

z = 45

def printVal(a = 1, x = 2):
	print("Printing values.")

	print ("Value of a is {}".format(a))
	print ("Value of x is {}".format(x))

	# Pick global value for this variable
	global z

	print ("Value of global z is {}".format(z))

def dump(*args, **vargs):
	print("Dumping values.")
	print(args)
	print(vargs)

printVal(5, 14)
printVal(x = 45)

dump(1, 2, 3, 4, 5)
dump(45, 65, "String", name="Ravi Malik")
