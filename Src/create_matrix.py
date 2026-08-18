import math

def gen_mat(size: int = 0):
    new_mat = []

    for k in range(size):
        ligne = [0.0] * size
        new_mat.append(ligne)
    return new_mat

def matrix_identitie(mat_init: list) -> list:
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

def create_matrix(src: list or str = "", cols: int = 0, is_key_matrix: bool = False) -> list:
    matrix = []
    if is_key_matrix:
        # Pad the key with null characters to make its length a perfect square
        # for a square matrix of cols x cols
        padded_src = str(src).ljust(cols * cols, '\0')
        row = cols
    else:
        padded_src = src
        row = math.ceil(len(src) / cols)
    for i in range(row):
        row_data = [0] * cols
        for j in range(cols):
            index = i * cols + j
            if index < len(padded_src):
                row_data[j] = ord(padded_src[index])
        matrix.append(row_data)
    return matrix

def find_size(src: list or str) -> int:
    size = len(src)
    square = find_min_square(size)
    row = int(math.sqrt(square))
    return row
