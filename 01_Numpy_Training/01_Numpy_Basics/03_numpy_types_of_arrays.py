"""
Different Types of Numpy Arrays:
    -All zeros Array
    -All ones Array
    -Any Other Numbers
"""
import numpy as np


# All O's Array
print("An np array containing 0's: \n{}".format(np.zeros((2, 3))))


# All 1's Array
print("An np array containing 1's: \n{}".format(np.ones((2, 3, 3))))

# Any other Numbers:
print("Any other Number: \n{}".format(np.full((2, 2), 255)))

# Matrix of Random Numbers
print("Printing Random numpy array: \n{}".format(np.random.rand(4, 2)))

# Random integer Values
print("integer Random array: \n{}".format(np.random.randint(0, 255, (3, 3))))

# Identity Matrix:
print("Identity Matrix: \n{}".format(np.identity(5)))

# Repeat an Array:
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print("Repeat of an Array: \n{}".format(r1))


"""
Note: Problem Regarding Copying numpy Arrays
"""
a = np.array([1, 2, 3])
# b = a
b = a.copy()
b[0] = 100
print(a)
print(b)
