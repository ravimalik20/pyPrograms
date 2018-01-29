#! /usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt
from random import randrange

data = [randrange(0, 100) for i in range(20)]
data = np.array(data)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jly', 'Aug', 'Sep', 'Oct',
	'Nov', 'Dec']

plt.plot(data, c='Green', ls="--", marker="s", label="random ints")
plt.xticks(list(range(0, 12)), months, rotation='vertical')
plt.show()
