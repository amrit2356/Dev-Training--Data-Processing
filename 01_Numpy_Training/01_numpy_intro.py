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
b = np.array([[1, 2, 3], [4, 5, 6]],dtype = 'int16')
print(b)

# Get Dimensions of Numpy Array
print("Dimension of Numpy Array {}".format(b.ndim))

# Get Shape(rows,col) of the Numpy Array
rows, col = b.shape
print("Rows: {} and Columns {}".format(rows, col))

# Get Datatype of the Numpy Array
data_type = b.dtype 
print("Datatype of the given Numpy array: {}".format(data_type))

# Get item size of numpy array
print("Memory Consumed by an item in np array: {}".format(b.itemsize))

# Get total size of the numpy array
print("No of Elements: {}".format(b.size))
print("Total Size of Numpy Array: {}".format(b.size*b.itemsize))