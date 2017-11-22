#! /usr/bin/python3

# Modes available: r, w, a
# Text Mode: t, binary Mode: b

import os

verse = '''
His palms are sweaty
Kneas weak, arms are heavy
There's vomit on his sweater already
Mom's spaghetti
He's nervous, but on the surface he looks calm and ready
do drop bomb's, but he keeps on forgettin
what he wrote down
the whole crowd grows so loud
he open's his mouth
but the word's won't come out
he's chokin, how?!
evrybody's jokin now
the clock's run out
time's up over, blow!!
'''

filename = "loose_yourself_verse1.txt"

f = open(filename, 'w')
f.write(verse)
f.close()

f = open(filename, 'r')
while True:
	line = f.readline()
	if (len(line) == 0):
		break

	print (line)

f.close()

# cleanup
os.remove(filename)
