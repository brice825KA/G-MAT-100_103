import math

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


