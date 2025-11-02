# Function to check if a list is a valid matrix
def is_matrix(my_list):
    if type(my_list) != list or len(my_list) == 0:
        return False

    for row in my_list:
        if type(row) != list:
            return False

    first_row_length = len(my_list[0])
    for row in my_list:
        if len(row) != first_row_length:
            return False

    return True

# Function to add two matrices
def add_matrices(mat1, mat2):
    # First, check if both are matrices
    if not is_matrix(mat1) or not is_matrix(mat2):
        return "One or both inputs are not valid matrices."

    # Check if the matrices are the same size
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices are not the same size, so they can't be added."

    result = []

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] * mat2[i][j])
        result.append(row)

    return result
def diff_matrices(mat1, mat2):
    # First, check if both are matrices
    if not is_matrix(mat1) or not is_matrix(mat2):
        return "One or both inputs are not valid matrices."

    # Check if the matrices are the same size
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices are not the same size, so they can't be added."

    result = []

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] - mat2[i][j])
        result.append(row)

    return result
    
def mul_matrices(mat1, mat2):
    # First, check if both are matrices
    if not is_matrix(mat1) or not is_matrix(mat2):
        return "One or both inputs are not valid matrices."

    # Check if the matrices are the same size
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices are not the same size, so they can't be added."

    result = []

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] * mat2[i][j])
        result.append(row)

    return result
matrix1 = [[1, 2,7], [3, 4,2]]
matrix2 = [[5, 6,8], [7, 8,5]]

sum_matrix = add_matrices(matrix1, matrix2)
diff_matrix= diff_matrices(matrix1,matrix2)
mul_matrix= mul_matrices(matrix1,matrix2)

print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)
print("Sum Matrix:", sum_matrix)
print("difference of Matrix:", diff_matrix)
print("multiplication of the items of Matrix:", mul_matrix)
