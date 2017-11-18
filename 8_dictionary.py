def printDict(d):
	for key, val in d.items():
		print("{0} : {1}".format(key, val))
	print ""

values = {
	'name' : 'Ravi Malik',
	'email' : 'ravimalik2364@gmail.com',
	'abc' : 'xyz'
}

printDict(values)

values['homepage'] = "https://ravimalik20.github.io/"
printDict(values)

del values['abc']
printDict(values)

if 'email' in values:
	print(values['email'])
