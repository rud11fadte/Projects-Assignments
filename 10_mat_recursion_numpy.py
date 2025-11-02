# ==========================================
# Program 1: Using NumPy for Sorting, Transpose, and Sum
# ==========================================
import numpy as np

print("\n--- NumPy Operations ---")

arr1 = np.array([[3, 1, 5], [4, 0, 2]])

print("Original array:\n", arr1)

# Sorting of list
sorted_arr1 = np.sort(arr1, axis=1)
print("Sorted array (axis=1):\n", sorted_arr1)

# Transpose of list
transpose_arr1 = arr1.T
print("Transpose of array:\n", transpose_arr1)

# Sum of list
sum_arr1 = np.sum(arr1)
print("Sum of all elements:", sum_arr1)


# ==========================================
# Program 2: Sorting and Transpose Without NumPy
# ==========================================

print("\n--- Manual List Operations ---")

# Sorting manually
list1 = [[3, 1, 5], [4, 0, 2]]
for row in list1:
    row.sort()
print("Sorted manually:", list1)

# Transpose manually
matrix1 = [[3, 1, 5], [4, 0, 2]]
rows = len(matrix1)
cols = len(matrix1[0])
transpose1 = []

for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix1[j][i])
    transpose1.append(row)
print("Transpose manually:", transpose1)

# Sum of list using recursion
nums1 = [3, 1, 5, 4, 0, 2]

def sumlist(nums):
    return sumListItr(nums, len(nums) - 1)

def sumListItr(lst, index):
    if index < 0:
        return 0
    return lst[index] + sumListItr(lst, index - 1)

print("Sum using recursion:", sumlist(nums1))


# ==========================================
# Program 3: Organized Matrix Utilities + NumPy Sorting
# ==========================================

print("\n--- Matrix Utilities ---")

# Sorting a 2D list (method 1)
lst1 = [[3, 1, 5], [4, 0, 2]]
for row in lst1:
    row.sort()
print("Sorted (method 1):", lst1)

# Sorting a 2D list (method 2)
lst2 = [[3, 1, 5], [4, 0, 2]]
sorted_list2 = [sorted(row) for row in lst2]
print("Sorted (method 2):", sorted_list2)


# Function to check if a structure is a valid matrix
def is_matrix(data):
    if not isinstance(data, list) or not data:
        return False
    row_length = len(data[0])
    for row in data:
        if not isinstance(row, list):
            return False
        if len(row) != row_length:
            return False
    return True


# Function to transpose a matrix
def transpose_matrix(m):
    if not is_matrix(m):
        return False
    num_rows = len(m)
    num_cols = len(m[0])
    new_matrix = []
    for i in range(num_cols):
        new_row = []
        for j in range(num_rows):
            new_row.append(m[j][i])
        new_matrix.append(new_row)
    return new_matrix


# Testing transpose
m2 = [[3, 1, 5], [4, 0, 2]]
print("Transpose of matrix:", transpose_matrix(m2))


# Sum of list using recursion (independent)
def sum_list(nums):
    return sum_list_itr(nums, len(nums) - 1)

def sum_list_itr(lst, index):
    if index < 0:
        return 0
    return lst[index] + sum_list_itr(lst, index - 1)

n2 = [3, 1, 5, 4, 0, 2]
print("Sum of list:", sum_list(n2))


# Sorting using numpy (independent)
arr2 = np.array([[3, 1, 5], [4, 0, 2]])
sorted_arr2 = np.sort(arr2, axis=1)
print("Sorted using NumPy:\n", sorted_arr2)
