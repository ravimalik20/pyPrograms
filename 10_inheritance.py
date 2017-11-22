#! /usr/bin/python3

class SchoolMember:
	def __init__(self, name, age):
		self.name = name
		self.age = age

		print ("Initialized school member: {}".format(self.name))

	def tell(self):
		""" Tell my details """

		print ("Name: {1} | Age: {0}".format(self.age, self.name), end = " | ")

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary

		print ("Initialized teacher: {}".format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print ("Salary: {}".format(self.salary))

class Student(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks

		print ("Initialized student: {}".format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print ("Marks: {}".format(self.marks))

teacher = Teacher("Simon Sinek", 35, "20M")
student = Student("Ravi Malik", 24, "B+")

members = (teacher, student)

for member in members:
	member.tell()
