from random import random
from decimal import Decimal

def randrange(start, stop):
    """
    Returns a random float between start and stop
    """
    start = Decimal(start)
    stop = Decimal(stop)
    return round(start + (stop - start) * Decimal(random()), 4)

def check_matrix_square(matrix):
    """
    Checks if the matrix is square
    """
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    return True

def swap_rows(matrix, i, j):
    """
    Swaps two rows in a matrix
    """
    try:
        matrix[i], matrix[j] = matrix[j], matrix[i]
    except IndexError:
        print("Ошибка при перестановке строк")
        return

def swap_cols(matrix, i, j):
    """
    Swaps two columns in a matrix
    """
    try:
        for row in matrix:
            row[i], row[j] = row[j], row[i]
    except IndexError:
        print("Ошибка при перестановке столбцов")
        return

def force_diagonal_dominance(matrix, b):
    """
    Makes a matrix diagonally dominant by swapping rows
    """
    n = len(matrix)
    for i in range(n):
        max_in_row = Decimal(0)
        max_col = Decimal(0)
        for j in range(n):
            if abs(matrix[i][j]) > max_in_row:
                max_in_row = abs(matrix[i][j])
                max_col = j
        if max_col != i:
            swap_rows(matrix, i, max_col)
            swap_rows(b, i, max_col)

def check_diagonal_dominance(matrix):
    """
    Checks if a matrix is diagonally dominant
    """
    n = len(matrix)
    strict_flag = False
    for i in range(n):
        sum_in_row = Decimal(0)
        for j in range(n):
            sum_in_row += abs(matrix[i][j])
        if abs(matrix[i][i]) < sum_in_row - abs(matrix[i][i]):
            return False
        if abs(matrix[i][i]) > sum_in_row - abs(matrix[i][i]):
            strict_flag = True
    return strict_flag

def get_matrix_norm(matrix):
    """
    Returns the norm of a matrix
    """
    n = len(matrix)
    norm = Decimal(0)
    for i in range(n):
        sum_in_row = Decimal(0)
        for j in range(n):
            sum_in_row += abs(matrix[i][j])
        norm = max(norm, sum_in_row)
    return norm

def get_vector_norm(vector):
    """
    Returns the norm of a vector
    """
    n = len(vector)
    norm = Decimal(0)
    for i in range(n):
        norm += vector[i] ** Decimal(2)
    return norm ** Decimal(0.5)

def split_matrix(matrix):
    """
    Splits a matrix into A and b
    """
    A = [row[:-1] for row in matrix]
    b = [row[-1] for row in matrix]
    return A, b

def add_vectors(vector1, vector2):
    """
    Adds two vectors
    """
    n = len(vector1)
    result = [Decimal(0) for _ in range(n)]
    for i in range(n):
        result[i] = vector1[i] + vector2[i]
    return result

def subtract_vectors(vector1, vector2):
    """
    Subtracts two vectors
    """
    n = len(vector1)
    result = [Decimal(0) for _ in range(n)]
    for i in range(n):
        result[i] = vector1[i] - vector2[i]
    return result

def multiply_matrix_vector(matrix, vector):
    """
    Multiplies a matrix by a vector
    """
    n = len(matrix)
    result = [Decimal(0) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i] += matrix[i][j] * vector[j]
    return result
