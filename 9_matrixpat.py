# Function to check if input is a valid matrix
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

# Function to check if a matrix is sparse
def is_sparse_matrix(matrix):
    if not is_matrix(matrix):
        return "Input is not a valid matrix."
    total_elements = len(matrix) * len(matrix[0])
    zero_count = sum(1 for row in matrix for item in row if item == 0)
    return zero_count > total_elements / 2

# ✅ Function to get non-zero entries as [rows], [cols], [values]
def get_non_zero_components(matrix):
    if not is_matrix(matrix):
        return "Input is not a valid matrix."

    row_list = []
    col_list = []
    value_list = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                row_list.append(i)
                col_list.append(j)
                value_list.append(matrix[i][j])

    return [row_list, col_list, value_list]

# ✅ Function to check if a matrix is symmetric
def is_symmetric_matrix(matrix):
    if not is_matrix(matrix):
        return "Input is not a valid matrix."

    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        return False  # Only square matrices can be symmetric

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Example matrix
matrix1 = [
    [0, 2, 0],
    [2, 0, 4],
    [0, 4, 0]
]

# Check if matrix is sparse
print("Is matrix sparse?", is_sparse_matrix(matrix1))

# Check if matrix is symmetric
print("Is matrix symmetric?", is_symmetric_matrix(matrix1))

# Get and print non-zero entries in [rows, cols, values] format
components = get_non_zero_components(matrix1)
print("Non-zero entries as:")
for comp in components:
    print(comp)

