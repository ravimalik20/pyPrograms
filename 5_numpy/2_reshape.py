import numpy as np

a = np.array(range(20))
print (a)

# Reshape it to a 5x4 matrix
a = np.reshape(a, (5, 4))
print (a)

# Fortran style reshape
b = np.array(range(20))
print (b)
b = np.reshape(b, (5, 4), 'F')
print (b)
