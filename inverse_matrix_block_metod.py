from time import clock_gettime
import numpy as np


def is_det_not_null(matrix: np.ndarray):
    """
    docstring
    """

    if check_square_matrix(matrix):
        if np.linalg.det(matrix) == 0:
            print("det(matrix) = 0")
            return False
        else:
            return True
    return False


def check_square_matrix(matrix: np.ndarray):
    """
    docstring
    """
    if matrix.shape[0] == matrix.shape[1]:
        return True

    print("matrix isn't square")
    return False


def cell_based_inverse_matrix_solver(matrix: np.ndarray):
    """

    Функция на вход получает матрицу в numpy.ndarray, для которой необходимо найти обратную матрицу

    Возвращает обратную матрицу в numpy.ndarray
    
    ---
    Матрица 0-3 в А располагаются следующим образом: 

    0 1

    2 3

    ---


    """
    if is_det_not_null(matrix):

        dim_num = matrix.shape[0]
        num_i = dim_num - 1

        arr_matrix_A = []
        # матрица 11
        arr_matrix_A.append(matrix[0:num_i, 0:num_i])
        # матрица 12
        arr_matrix_A.append(matrix[0:num_i, num_i:dim_num])
        # матрица 21
        arr_matrix_A.append(matrix[num_i:dim_num, 0:num_i])
        # матрица 22
        arr_matrix_A.append(matrix[num_i: dim_num, num_i:dim_num])

        if arr_matrix_A[0].shape[0] > 1:
            A_0_inv = cell_based_inverse_matrix_solver(arr_matrix_A[0])
        elif arr_matrix_A[0].shape[0] == 1:
            A_0_inv = np.linalg.inv(arr_matrix_A[0])

        matrix_D = np.zeros(matrix.shape)

        # 22
        matrix_D[num_i: dim_num, num_i:dim_num] = np.linalg.inv(
            arr_matrix_A[3] - np.dot(np.dot(arr_matrix_A[2], A_0_inv), arr_matrix_A[1]))
        # 12
        matrix_D[0:num_i, num_i:dim_num] = np.dot(np.dot(
            (-1 * A_0_inv), arr_matrix_A[1]), matrix_D[num_i: dim_num, num_i:dim_num])
        # 21
        matrix_D[num_i:dim_num, 0:num_i] = np.dot(
            np.dot((-1 * matrix_D[-1][-1]), arr_matrix_A[2]), A_0_inv)
        # 11
        matrix_D[0:num_i, 0:num_i] = np.dot(A_0_inv, (np.eye(
            num_i) - np.dot(arr_matrix_A[1], matrix_D[num_i:dim_num, 0:num_i])))

        return matrix_D

    raise ValueError("Неправильная матрица")


def main():
    """
    main function
    """
    # a = np.eye(2)
    # cell_based_inverse_matrix_solver(a)

    a = np.array([[2, 5, 7],
                  [6, 3, 4],
                  [5, -2, -3]])
    

    

    print("Обратная матирица, найденная методом разбиением на клетки")
    start_time = clock_gettime(0)
    print(cell_based_inverse_matrix_solver(a))
    print(clock_gettime(0) - start_time)


    print("Обратная матирица, найденная встроенным методом в NumPy")
    start_time = clock_gettime(0)
    print(np.linalg.inv(a))
    print(clock_gettime(0) - start_time)

    print(np.dot(a, cell_based_inverse_matrix_solver(a)))
    print()

    print(np.dot(a, np.linalg.inv(a)))
    print()

    # print(np.array_equiv(cell_based_inverse_matrix_solver(a), np.linalg.inv(a)))


if __name__ == "__main__":
    main()
