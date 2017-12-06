#! /usr/bin/python3

class Records:
	def __init__(self):
		self.records = []

	def __lt__(self, other):
		return len(self.records) < len(other.records)

	def __gt__(self, other):
		return len(self.records) > len(other.records)

	def __getitem__(self, key):
		return self.records[key]

	def __len__(self):
		return len(self.records)

	def __del__(self):
		print ("Object is being destroyed!")

	def append(self, val):
		self.records.append(val)

	def pop(self):
		return self.records.pop()

	def __str__(self):
		return "{}".format(self.records)

r1 = Records()
r2 = Records()

for i in range(1, 20):
	r1.append(i)

for i in range(1, 20, 2):
	r2.append(i)

print (r1 > r2)

print (r1[4], r2[5])

print(r1, r2)
