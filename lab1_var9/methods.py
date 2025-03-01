from libs.math import *
def simple_iteration_method(C, d, eps, max_iter=10000):
    n = len(C)
    x = [0 for _ in range(n)]
    x_new = [0 for _ in range(n)]
    error = 1e30
    last_error = 1e30
    iters = 0

    print(f"Норма матрицы C: {get_matrix_norm(C)}")
    for i in range(max_iter):
        x_new = add_vectors(multiply_matrix_vector(C, x), d)
        error = get_vector_norm(subtract_vectors(x_new, x))
        if error < eps:
            iters = i
            break
        if error > last_error:
            return [None, None, None]
        last_error = error
        x = x_new

    return [x, iters, error]
    