import sys
from libs.math import randrange

def terminal_input_vector():
    try:
        vector = list(map(int, input().split()))
        return vector
    except ValueError:
        print("Неверный формат ввода")
        sys.exit(1)

def terminal_input_matrix():
    try:
        matrix = []
        for line in sys.stdin.readlines():
            matrix.append(list(map(int, line.split())))
        return matrix
    except ValueError:
        print("Неверный формат ввода")
        sys.exit(1)

def terminal_input_accuracy():
    try:
        return float(input())
    except ValueError:
        print("Неверный формат ввода")
        sys.exit(1)

def file_input_matrix(filename):
    try:
        with open(filename, "r") as file:
            matrix = []
            for line in file:
                matrix.append(list(map(int, line.split())))
        return matrix
    except FileNotFoundError:
        print("Файл не найден")
        sys.exit(1)
    except PermissionError:
        print("Недостаточно прав")
        sys.exit(1)
    except ValueError:
        print("Неверный формат ввода")
        sys.exit(1)

def file_input_accuracy(filename):
    try:
        with open(filename, "r") as file:
            return float(file.readline())
    except FileNotFoundError:
        print("Файл не найден")
        sys.exit(1)
    except PermissionError:
        print("Недостаточно прав")
        sys.exit(1)
    except ValueError:
        print("Неверный формат ввода")
        sys.exit(1)

def random_input_matrix(n):
    matrix = [[0 for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        for j in range(n + 1):
            matrix[i][j] = randrange(-5, 5)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(*row)


def file_input():
    filename = input("Введите имя файла с матрицей: ")
    matrix = file_input_matrix(filename)
    
    filename = input("Введите имя файла с точностью: ")
    eps = file_input_accuracy(filename)

    return matrix, eps

def console_input():
    print("Введите матрицу:")
    matrix = terminal_input_matrix()

    print("Введите точность:")
    eps = terminal_input_accuracy()

    return matrix, eps

def random_input():
    try:
        n = int(input("Введите размерность матрицы: "))
    except ValueError:
        print("Неверный формат ввода")
        sys.exit(1)
    matrix = random_input_matrix(n)
    print("Матрица:")
    print_matrix(matrix)

    print("Введите точность:")
    eps = terminal_input_accuracy()
    
    return matrix, eps