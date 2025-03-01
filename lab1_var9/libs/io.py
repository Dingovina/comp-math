import sys
from libs.math import randrange
from libs.mapper import string_to_decimal
from decimal import Decimal

def terminal_input_vector():
    """
    Reads a vector of numbers from terminal input and converts them to Decimal
    """
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
    """
    Reads a matrix of numbers from terminal input and converts them to Decimal
    """
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
    """
    Reads a decimal number representing accuracy from terminal input
    """
    try:
        return string_to_decimal(input())
    except ValueError:
        print("Неверный формат ввода")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Прервано пользователем")
        sys.exit(1)

def file_input_matrix(filename):
    """
    Reads a matrix of numbers from a file and converts them to Decimal
    """
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
    """
    Reads a decimal number representing accuracy from a file
    """
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
    """
    Generates an n x (n+1) matrix with random decimal numbers
    """
    matrix = [[Decimal(0) for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        for j in range(n + 1):
            matrix[i][j] = Decimal(randrange(-5, 5))
    return matrix

def print_matrix(matrix):
    """
    Prints the matrix to the console
    """
    for row in matrix:
        print(*row)

def file_input():
    """
    Reads matrix and accuracy from files specified by the user
    """
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
    """
    Reads matrix and accuracy from terminal input
    """
    print("Введите матрицу:")
    matrix = terminal_input_matrix()

    print("Введите точность:")
    eps = terminal_input_accuracy()

    return matrix, eps

def random_input():
    """
    Generates a random matrix and reads accuracy from terminal input
    """
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
