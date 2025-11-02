# Function to multiply two matrices
def multiply_matrices(A, B):
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        print("Matrix multiplication not possible ")
        return None

    # Create result matrix filled with 0s
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Multiply the matrices
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Function to print a matrix nicely
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Main part of the code
A = [
    [1],
    [4],
    [7]
]

B = [
    [1,2,3]
]

# Call the function
product = multiply_matrices(A, B)

# Print the result
if product:
    print("Matrix A × B = ")
    print_matrix(product)

