import sys
from libs.math import randrange
from libs.mapper import string_to_decimal
from decimal import Decimal

def terminal_input_vector():
    try:
        vector = list(map(string_to_decimal, input().split()))
        return vector
    except ValueError:
        print("Неверный формат ввода")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Прервано пользователем")
        sys.exit(1)

def terminal_input_matrix():
    try:
        matrix = []
        for line in sys.stdin.readlines():
            matrix.append(list(map(string_to_decimal, line.split())))
        return matrix
    except ValueError:
        print("Неверный формат ввода")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Прервано пользователем")
        sys.exit(1)

def terminal_input_accuracy():
    try:
        return string_to_decimal(input())
    except ValueError:
        print("Неверный формат ввода")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Прервано пользователем")
        sys.exit(1)

def file_input_matrix(filename):
    try:
        with open(filename, "r") as file:
            matrix = []
            for line in file:
                matrix.append(list(map(string_to_decimal, line.split())))
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
            return string_to_decimal(file.readline())
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
    matrix = [[Decimal(0) for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        for j in range(n + 1):
            matrix[i][j] = Decimal(randrange(-5, 5))
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(*row)


def file_input():
    try:
        filename = input("Введите имя файла с матрицей: ")
        matrix = file_input_matrix(filename)
        
        filename = input("Введите имя файла с точностью: ")
        eps = file_input_accuracy(filename)

        return matrix, eps
    except KeyboardInterrupt:
        print("Прервано пользователем")
        sys.exit(1)

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