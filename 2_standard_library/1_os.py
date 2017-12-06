#! /usr/bin/python3

import os
import shutil
from glob import glob

print ("Current working directory: {}".format(os.getcwd()))

os.mkdir("dir")
os.chdir("dir")
os.system("touch new_file.txt")

f = open("new_file.txt", "w")
f.write("Sample Text.")
f.close()

os.system("cat new_file.txt")
print("")
os.system("rm new_file.txt")
os.chdir("..")
os.rmdir("dir")

# Returns list of files matching the wildcard
print(glob("*.py"))
