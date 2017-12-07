#! /usr/bin/python3

from urllib.request import urlopen

with urlopen("http://ravimalik20.github.io/") as response:
	for line in response:
		val = line.decode("utf-8")
		print(val)


