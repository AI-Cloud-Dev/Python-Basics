import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("shape:", arr.shape)
print("Mean:", arr.mean())
print("Normalized:", arr/arr.max())

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:", matrix)
print("Firstrow:", matrix[0])
print("shape:", matrix.shape)
print("mean: ", matrix.mean())
print("Element at [1,2]: ", matrix[1, 2])


mat = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print("Array:", mat)
print("Second Row:", mat[1])
print("Element at: ", mat[0, 1])