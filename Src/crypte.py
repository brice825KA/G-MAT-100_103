from Src.create_matrix import find_size, gen_mat, create_matrix

def crypte(message: str, key: str) -> str:
    size = find_size(key)
    matrix_key = create_matrix(key, size)
    matrix_message = create_matrix(message, size)
    print(f"Size: {size}")
    print(f"Matrix Key: {matrix_key}")
    print(f"Matrix Message: {matrix_message}")
    