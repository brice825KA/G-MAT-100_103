from Src.create_matrix import find_size, create_matrix
from Src.mulmat import multimat

def crypte(message: str, key: str):
    size = find_size(key)
    matrix_key = create_matrix(key, size, is_key_matrix=True)
    matrix_message = create_matrix(message, size)
    print(f"Matrix Result: {multimat(matrix_message, matrix_key)}")
    