#! /usr/bin/python3

import pickle, os

shoplist = ['kale', 'spinach', 'butter', 'chicken', 'half n half']

shoplist_file = 'shoplist.data'

print ("List before pickle: {}".format(shoplist))

f = open(shoplist_file, "wb")
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplist_file, "rb")
storedlist = pickle.load(f)
print ("List retreived after pickle: {}".format(storedlist))

#cleanup
os.remove(shoplist_file)
