import math

def gen_mat(size):
    new_mat = []

    for k in range(size):
        ligne = [0.0] * size
        new_mat.append(ligne)
    return new_mat

def matrix_identitie(mat_init):
    size = int(math.sqrt(len(mat_init)))
    new_mat = gen_mat(size)
    
    for i in range(len(new_mat)):
        for j in range(len(new_mat[i])):
            if i == j:
                new_mat[i][j] = 1.0
            else:
                new_mat[i][j] = 0.0
    return new_mat


def find_min_square(n: int) -> int:
    square = n
    while 1:
        if math.sqrt(square) % 1 != 0:
            square += 1
        else:
            break
    return square

def create_matrix(src: list, cols: int, row: int) -> list:
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(src[i * cols + j])
    return matrix


