import numpy as np
from matplotlib import pyplot as plt
from random import randint

def randomList(n):
	return [randint(0, 100) for i in range(n)]

a = np.array(randomList(10))
b = np.array(randomList(10))
c = np.array(randomList(10))
d = np.array(randomList(10))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jly', 'Aug', 'Sep', 'Oct',
	'Nov', 'Dec']

plt.plot(a, c='black', ls="-", marker="s")
plt.plot(b, c='blue', ls="--", marker="d")
plt.plot(c, c='green', ls="-.", marker="o")
plt.plot(d, c='red', ls="-", marker="^")

plt.xticks(list(range(12)), months)

plt.show()
