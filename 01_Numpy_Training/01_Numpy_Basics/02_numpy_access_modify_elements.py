"""
Accessing/Changing specific elements, rows, columns
"""

import numpy as np

# Creation of 2-D Array
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

"""
Indexing in Numpy: [row,col]
    row -> It points to the row index
    col -> It points to the column index.

Slicing in Numpy:
    ':' - this operator is used to select series of elements between 2 indices.
        - also used in conjunction to act as a stepsize.

    Format:
    [rowstart: rowend: row_stepsize, colstart: colend: col_stepsize]

Note: You can use lists([0,2,5,5]) to select specific indices.

Traversal in Numpy:
    +ve Index Value: 0 to n-1
    -ve Index Value: -1 to -(n-2)

Note: if you wanna traverse or print output in reverse order, use -ve Index.
"""


# Getting a specific element from numpy array
# indexing starts from 0 to n-1
print("Element in 2nd Row, 6th Column is: {}".format(a[1, 5]))

# Getting a specific row:
print("\n")
print("Elements in 1st Row: {}".format(a[0, :]))
print("Elements in 2nd Row: {}".format(a[1, :]))

# Getting a specific column:
print("\n")
print("Elements in 4th Column: {}".format(a[:, 3]))
print("Elements in 7th Column: {}".format(a[:, 6]))

# Numpy Slicing
# [start_index:end_index:stepsize]
print("\n")
print("Element in the first Row,slicing even numbers: {} ".format(a[0, 1:6:2]))

# Slicing using -ve numbers
print("\n")
rev_ind = a[0, :-1]
slice_rev = a[0, 1:-1:2]
print("-ve index to travel np array in rev order a[0,:-1]: {}".format(rev_ind))
print("slicing set of values(using -ve slicing): {}".format(slice_rev))


"""
Modification of element value in Numpy Array by:
    - specifying the row & index value.
    - using ':' operator, to change  different sets of elements.
"""


# Modifying an element in a specific function
a[1, 5] = 20
print("\n")
print("Modified element in 2nd Row, 6th Column: {}".format(a))

# Modifying a series of elements:
a[:, 2] = [1, 2]
print("Modifying Series of elements: {}".format(a))
