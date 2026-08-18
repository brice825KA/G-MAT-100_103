def multimat(matone: list, mattwo: list) -> list:
    rows_one = len(matone)
    cols_one = len(matone[0]) if rows_one > 0 else 0
    cols_two = len(mattwo[0]) if len(mattwo) > 0 else 0

    # Check for compatible dimensions for matrix multiplication
    if cols_one != len(mattwo):
        raise ValueError("Matrix dimensions are not compatible for multiplication. The number of columns in matone must be equal to the number of rows in mattwo.")
    new_mat = [[0] * cols_two for _ in range(rows_one)]

    for i in range(rows_one):
        for j in range(cols_two):
            sum = 0
            for k in range(cols_one):
                sum += (matone[i][k] * mattwo[k][j]) 
            new_mat[i][j] = sum
    return new_mat
