"""
Mathematics Involved with Numpy.
    - Scalar Arith. Operations:(Addition,Subtraction,Multiplication,Division)
"""

import numpy as np


a = np.array([1, 2, 3, 4])
print(a)

# Scalar Arithmethic Operations(with a no)
# Addition
print("Add all elements by 2: {}".format(a+2))

# Subtraction
print("Sub all elements by 2: {}".format(a-2))

# Multiplication
print("Multiply all elements by 2: {}".format(a*2))

# Division
print("Divide all elements by 2: {}".format(a/2))


# Arithmetic Operations(with another np array)
b = np.array([1, 0, 1, 0])
print("Addition of 2 np arrays: {}".format(a+b))
print("Subtraction of 2 np arrays: {}".format(a-b))
