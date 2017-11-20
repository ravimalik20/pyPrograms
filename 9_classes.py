class Robot:
	population = 0

	def __init__(self, name):
		self.name = name

		print("Initializing a robot with name: {}".format(name))

		Robot.population += 1

	def die(self):
		print("Destroying robot: {}".format(self.name))

		Robot.population -= 1

	def sayHi(self):
		print("Hi. My name is {}".format(self.name))

	@classmethod
	def howMany(cls):
		print("Current number of robots are: {:d}".
			format(cls.population))

if __name__ == "__main__":
	droid1 = Robot("R2-D2")
	droid1.sayHi()
	Robot.howMany()

	droid2 = Robot("C-3PO")
	droid2.sayHi()
	Robot.howMany()

	print("\nRobots can do some work here.\n")
	print("Robots have finished their work. So let's destroy them.")

	droid1.die()
	droid2.die()
	Robot.howMany()
