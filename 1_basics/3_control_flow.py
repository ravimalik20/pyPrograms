#! /usr/bin/python3

running = True

while running:
	val = int(input("Enter a number:"))

	if val == 40:
		running = False
		print("Bang on target!")
	elif val < 40:
		print("Your guess is a bit low.")
	else:
		print("Your guess is a bit high")

# Starting from 10 and just short of 45
for i in range(10, 45):
	print(i, end=", ")
else:
	print('The for loop is over')

# Increment in steps of 2
for i in range(10, 45, 2):
	print(i, end=", ")
else:
	print("The for loop is over")
