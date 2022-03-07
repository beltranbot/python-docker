import numpy as np

a = np.random.rand(3) # generate a list of 3 random elements
print(a)

a = np.random.rand(3, 3) # generate a matrix of 3x3
print(a)

a = np.random.randint(20, 30, (3, 4)) # random 3x4 matrix with elements of value 20 to 30
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.random.shuffle(arr)
print(arr) # shuffle elements

np.random.seed(1) # different of the random library seed

print(np.random.rand(3, 3))
