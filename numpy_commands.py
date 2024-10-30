import numpy as np

# 1. np.random.rand() - Generates an array of random numbers between 0 and 1
print("1. np.random.rand():")
random_array = np.random.rand(2, 3)
print(random_array, "\n")

# 2. np.sum() - Returns the sum of array elements over a specified axis
print("2. np.sum():")
array = np.array([[1, 2], [3, 4]])
print(np.sum(array))  # Sum of all elements
print(np.sum(array, axis=0))  # Sum by column
print(np.sum(array, axis=1), "\n")  # Sum by row

# 3. np.std() - Calculates the standard deviation of the array elements
print("3. np.std():")
print(np.std(array), "\n")

# 4. np.median() - Finds the median of array elements
print("4. np.median():")
print(np.median(array), "\n")

# 5. np.mean() - Calculates the mean (average) of the array elements
print("5. np.mean():")
print(np.mean(array), "\n")

# 6. np.where() - Returns the indices of elements that satisfy a condition
print("6. np.where():")
condition_array = np.array([1, 2, 3, 4, 5])
print(np.where(condition_array > 2), "\n")  # Indices where condition is true

# 7. np.unique() - Finds the unique elements of an array
print("7. np.unique():")
repeated_array = np.array([1, 2, 2, 3, 4, 4, 4])
print(np.unique(repeated_array), "\n")

# 8. np.hstack() - Stacks arrays in sequence horizontally (column-wise)
print("8. np.hstack():")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.hstack((a, b)), "\n")

# 9. np.vstack() - Stacks arrays in sequence vertically (row-wise)
print("9. np.vstack():")
print(np.vstack((a, b)), "\n")

# 10. np.array() - Creates a new array from a list or list of lists
print("10. np.array():")
array_from_list = np.array([1, 2, 3, 4, 5])
print(array_from_list, "\n")

# 11. np.zeros() - Creates an array filled with zeros
print("11. np.zeros():")
zeros_array = np.zeros((2, 3))  # 2x3 matrix of zeros
print(zeros_array, "\n")

# 12. np.ones() - Creates an array filled with ones
print("12. np.ones():")
ones_array = np.ones((2, 3))  # 2x3 matrix of ones
print(ones_array, "\n")

# 13. np.eye() - Creates a 2D identity matrix
print("13. np.eye():")
identity_matrix = np.eye(3)
print(identity_matrix, "\n")

# 14. np.arange() - Creates an array with a range of numbers
print("14. np.arange():")
range_array = np.arange(0, 10, 2)  # Start from 0 to 10 with a step of 2
print(range_array, "\n")

# 15. np.linspace() - Creates an array with evenly spaced numbers over a specified interval
print("15. np.linspace():")
linear_space = np.linspace(0, 1, 5)  # 5 numbers from 0 to 1
print(linear_space, "\n")

# 16. np.reshape() - Reshapes an array without changing its data
print("16. np.reshape():")
reshaped_array = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(reshaped_array, "\n")

# 17. np.transpose() - Transposes the axes of an array
print("17. np.transpose():")
transposed_array = np.transpose(reshaped_array)
print(transposed_array, "\n")

# 18. np.flatten() - Flattens a multi-dimensional array into a 1D array
print("18. np.flatten():")
flattened_array = reshaped_array.flatten()
print(flattened_array, "\n")

# 19. np.concatenate() - Joins a sequence of arrays along an existing axis
print("19. np.concatenate():")
concat_array = np.concatenate((a, b), axis=0)
print(concat_array, "\n")

# 20. np.split() - Splits an array into multiple sub-arrays
print("20. np.split():")
split_array = np.array([1, 2, 3, 4, 5, 6])
print(np.split(split_array, 3))  # Split into 3 equal sub-arrays
