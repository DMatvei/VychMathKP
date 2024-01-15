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


def is_nondegenerate_matrix(matrix: np.ndarray):
    """
    docstring
    """

    if is_det_not_null(matrix):
        n = matrix.shape[0]

        for i in range(n):
            matrix_ = matrix[0:i, 0:i]
            if np.linalg.det(matrix_) == 0:
                print("matrix is degenerate")
                return False

        return True

    return False


def gen_matrix_for_LU(n):
    rng = np.random.default_rng()
    is_right_matrix = False
    matrix : np.ndarray
    while(not is_right_matrix):
        matrix = rng.random((n, n)) * 10 - 5
        if is_nondegenerate_matrix(matrix):
            is_right_matrix = True

    return matrix


def gen_matrix(n):
    rng = np.random.default_rng()
    is_right_matrix = False
    matrix : np.ndarray
    while(not is_right_matrix):
        matrix = rng.random((n, n)) * 10 - 5
        if is_det_not_null(matrix):
            is_right_matrix = True

    return matrix



def output_for_matrix(matrix : np.ndarray):


    string_ = "a = np.array(["

    n = matrix.shape[0]
    for i in range(n):
        string_matrix = "["
        for ii in range(n):
            string_matrix += str(matrix[i][ii]) + ", "

        string_matrix = string_matrix[:-2] + "]"

        string_ += string_matrix + ", \n"
    string_ = string_[:-3] + "])"
    


    print(string_)


def check_multiple_original_inv(matrix: np.ndarray, matrix_inv : np.ndarray):

    return np.dot(matrix, matrix_inv)


def check_multiple_det(matrix : np.ndarray, matrix_inv: np.ndarray):
    print("умножение определителей")
    app_value = np.dot(np.linalg.det(matrix), np.linalg.det(matrix_inv))
    absolute_error = abs(1 - np.dot(np.linalg.det(matrix), np.linalg.det(matrix_inv)))
    print(f'Абсолютная погрешность: {absolute_error}')
    print(f'Относительная погрешность: {(absolute_error / app_value) * 100} %')
    return app_value
    




def match_Cond(matrix, matrix_inv):
    """
    docstring
    """
    return np.linalg.norm(matrix) * np.linalg.norm(matrix_inv)


def main():
    for i in range(3, 11):
        # print(i)
        output_for_matrix(gen_matrix_for_LU(i))
        print("\n \n")




if __name__ == "__main__":
    main()