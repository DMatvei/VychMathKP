import numpy as np


def match_matrixLU(matrixA):
    n = len(matrixA)
    matrix_L = np.zeros((n, n))
    matrix_U = np.zeros((n, n))

    for i in range(n):
        matrix_L[i][i] = 1

    for j in range(n):
        matrix_U[0][j] = matrixA[0][j]

    # заполнениние l элементами столбец 1

    for i in range(1, n):
        matrix_L[i][0] = matrixA[i][0] / matrix_U[0][0]

    # заполнение матриц L и U

    for i in range(1, n):
        match_line_U(matrixA, matrix_U, matrix_L, i)

    return matrix_L, matrix_U


# функция для вычисления строки матрицы U

def match_line_U(matrixA, matrixU, matrixL, i):
    n = len(matrixA)

    for j in range(n):
        if i <= j:
            match_U(matrixA, matrixU, matrixL, i, j)
        elif i > j:
            match_line_L(matrixA, matrixU, matrixL, i, j)


# функция для вычисления l

def match_line_L(matrixA, matrixU, matrixL, i, j):

    matrixL[i][j] = (matrixA[i][j] - mathc_sum_lu(matrixL,
                     matrixU, i, j)) / matrixU[j][j]


def match_U(matrixA, matrixU, matrixL, i, j):

    matrixU[i][j] = matrixA[i][j] - mathc_sum_lu(matrixL, matrixU, i, j)


# функция для вычисления суммы l * u

def mathc_sum_lu(matrixL, matrixU, i, j):
    sum_num = 0
    if i > j:
        lim_k = j - 1
    else:
        lim_k = i - 1

    for k in range(lim_k + 1):
        sum_num += matrixL[i][k] * matrixU[k][j]

    return sum_num


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


def inv_lu(matrix):
    """
    docstring
    """
    if is_nondegenerate_matrix(matrix):
        pass

    raise ValueError("Не корректная матрица")


def main():

    
    
    
    
    
    pass

if __name__ == "__main__":
    main()