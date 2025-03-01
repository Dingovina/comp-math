from random import random

def randrange(start, stop):
    return round(start + (stop - start) * random(), 4)

def check_matrix_square(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    return True
def swap_rows(matrix, i, j):
    try:
        matrix[i], matrix[j] = matrix[j], matrix[i]
    except IndexError:
        print("Ошибка при перестановке строк")
        return

def swap_cols(matrix, i, j):
    try:
        for row in matrix:
            row[i], row[j] = row[j], row[i]
    except IndexError:
        print("Ошибка при перестановке столбцов")
        return

def force_diagonal_dominance(matrix, b):
    n = len(matrix)
    for i in range(n):
        max_in_row = 0
        max_col = 0
        for j in range(n):
            if abs(matrix[i][j]) > max_in_row:
                max_in_row = abs(matrix[i][j])
                max_col = j
        if max_col != i:
            swap_rows(matrix, i, max_col)
            swap_rows(b, i, max_col)

def check_diagonal_dominance(matrix):
    n = len(matrix)
    strict_flag = False
    for i in range(n):
        sum_in_row = 0
        for j in range(n):
            sum_in_row += abs(matrix[i][j])
        if abs(matrix[i][i]) < sum_in_row - abs(matrix[i][i]):
            return False
        if abs(matrix[i][i]) > sum_in_row - abs(matrix[i][i]):
            strict_flag = True
    return strict_flag

def get_matrix_norm(matrix):
    n = len(matrix)
    norm = 0
    for i in range(n):
        sum_in_row = 0
        for j in range(n):
            sum_in_row += abs(matrix[i][j])
        norm = max(norm, sum_in_row)
    return norm

def get_vector_norm(vector):
    n = len(vector)
    norm = 0
    for i in range(n):
        norm += vector[i] ** 2
    return norm ** 0.5

def split_matrix(matrix):
    A = [row[:-1] for row in matrix]
    b = [row[-1] for row in matrix]
    return A, b

def add_vectors(vector1, vector2):
    n = len(vector1)
    result = [0 for _ in range(n)]
    for i in range(n):
        result[i] = vector1[i] + vector2[i]
    return result

def subtract_vectors(vector1, vector2):
    n = len(vector1)
    result = [0 for _ in range(n)]
    for i in range(n):
        result[i] = vector1[i] - vector2[i]
    return result

def multiply_matrix_vector(matrix, vector):
    n = len(matrix)
    result = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i] += matrix[i][j] * vector[j]
    return result