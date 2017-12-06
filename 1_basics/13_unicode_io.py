#! /usr/bin/python3

import io, os

f = io.open("abc.txt", "wt", encoding = "utf-8")
f.write(u"This is a text!")
f.close()

text = io.open("abc.txt", encoding = "utf-8").read()
print(text)

# cleanup
os.remove("abc.txt")
