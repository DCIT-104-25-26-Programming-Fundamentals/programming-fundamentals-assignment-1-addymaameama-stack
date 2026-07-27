# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    m = []
    for i in range(rows):
        line = input(f"Enter row {i+1}: ").split()
        nums = [int(x) for x in line]
        m.append(nums)
    return m


def print_matrix(m):
    for row in m:
        for val in row:
            print(val, end="\t")
        print()
    print()


def transpose(m, rows, cols):
    # new matrix has cols x rows dimensions
    result = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(m[j][i])
        result.append(new_row)
    return result


def add_matrices(a, b, rows, cols):
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


def multiply_matrices(a, b, m, n, p):
    result = []
    for i in range(m):
        row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total = total + a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result


def part_a():
    print("PART A - TRANSPOSE")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    trans = transpose(matrix, rows, cols)
    print("Transposed Matrix:")
    print_matrix(trans)


def part_b():
    print("PART B - ADDITION")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Matrix A:")
    a = read_matrix(rows, cols)
    print("Matrix B:")
    b = read_matrix(rows, cols)

    result = add_matrices(a, b, rows, cols)

    print("\nMatrix A:")
    print_matrix(a)
    print("Matrix B:")
    print_matrix(b)
    print("A + B:")
    print_matrix(result)


def part_c():
    print("PART C - MULTIPLICATION")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A: "))
    p = int(input("Enter columns of Matrix B: "))
    # note: rows of B must equal n, we already asked for that above

    print("Matrix A:")
    a = read_matrix(m, n)
    print("Matrix B:")
    b = read_matrix(n, p)

    result = multiply_matrices(a, b, m, n, p)

    print("\nMatrix A:")
    print_matrix(a)
    print("Matrix B:")
    print_matrix(b)
    print("A x B:")
    print_matrix(result)


def main():
    part_a()
    print()
    part_b()
    print()
    part_c()


main()