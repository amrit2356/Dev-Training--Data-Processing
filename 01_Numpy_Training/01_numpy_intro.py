"""
Introduction to Numpy
    Numpy is a package designed for data processing, using multi dim arrays.
    It is faster than lists, because:
        -It takes a fixed type
        -It takes less bytes of memory.(Faster to Read).
        -No type checking(since datatype in np array is fixed).
        -It allocates contiguous memory (Traversing through memory is faster).
    Op Possible in Lists: insertion, deletion, appending, concatenation etc.
    Op Possible in Numpy: lots more :P.
"""
import numpy as np

# 1-D numpy Array
a = np.array([1, 2, 3])
print(a)

# 2-D numpy Array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
