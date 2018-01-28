import numpy as np

a = np.array(range(20)).reshape((5, 4))
b = np.array(range(20, 0, -1)).reshape((5, 4))

print (a)
print (b)

# divide one matrix by another
c = a / b
print (c)

# round each value of the matrix
print (np.matrix.round(c))
