from libs.methods import *
from libs.commands import *
from decimal import getcontext

def user_input():
    """
    Asks user for input type and provides the appropriate function.
    """
    try:
        input_id = input("Выберите тип ввода (1 - файл, 2 - терминал, 3 - случайный): ")
    except KeyboardInterrupt:
        print("Прервано пользователем")
        sys.exit(1)

    try:
        matrix, eps = INPUT_COMMANDS[input_id]()
    except KeyError:
        print("Неверный тип ввода")
        sys.exit(1)
    
    return matrix, eps

def main():
    """
    Program entry point.
    """
    getcontext().prec = 100
    matrix, eps = user_input()
    
    A, b = split_matrix(matrix)
    if not check_matrix_square(A):
        print("Матрица не квадратная")
        sys.exit(1)
    
    n = len(A)
    
    if check_diagonal_dominance(A):
        print("Матрица диагонально доминирующая")
    else:
        print("Матрица не диагонально доминирующая")
        force_diagonal_dominance(A, b)
        print("Преобразуем матрицу...")

    if not check_diagonal_dominance(A):
        print("Матрицу невозможно привести к диагонально доминирующей")
    else:
        print("Матрица приведена к диагонально доминирующей")
    
    x, iters, error = simple_iteration_method(A, b, eps)
    
    if x is None:
        print("Метод не сходится")
        sys.exit(1)

    print("Решение:")
    for i in range(n):
        print(f"x{i + 1} = {x[i]}")
    
    print(f"Количество итераций: {iters}")
    
    print(f"Погрешность: {error}")

if __name__ == '__main__':
    main()
