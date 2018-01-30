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

plt.plot(a, c='black', ls="-", marker="s", label="rand1")
plt.plot(b, c='blue', ls="--", marker="d", label="rand2")
plt.plot(c, c='green', ls="-.", marker="o", label="rand3")
plt.plot(d, c='red', ls="-", marker="^", label="rand4")

plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

plt.xticks(list(range(12)), months)

plt.show()
