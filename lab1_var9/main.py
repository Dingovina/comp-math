from methods import *
from commands import *

def user_input():
    input_id = input("Выберите тип ввода (1 - файл, 2 - терминал, 3 - случайный): ")

    try:
        matrix, eps = INPUT_COMMANDS[input_id]()
    except KeyError:
        print("Неверный тип ввода")
        sys.exit(1)
    
    return matrix, eps

def main():
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
    
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                C[i][j] = 0
            else:
                C[i][j] = -A[i][j] / A[i][i]
    
    d = [0 for _ in range(n)]
    for i in range(n):
        d[i] = b[i] / A[i][i]
    
    x, iters, error = simple_iteration_method(C, d, eps)
    
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
    