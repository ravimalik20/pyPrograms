#! /usr/bin/python3

from timeit import Timer

res = Timer("t=a; a=b; b=t", "a=1; b=2").timeit()

print ("Timing result: {}".format(res))
