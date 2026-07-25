
from Src.matrix_identitie import gen_mat

def multimat(matone, mattwo):
    size = len(matone)
    new_mat = gen_mat(size)
    sum = 0

    for i in range(size):
        for j in range(size):
            sum = 0
            for k in range(size):
                sum += (matone[i][k] * mattwo[k][j]) 
            new_mat[i][j] = sum
    return new_mat
