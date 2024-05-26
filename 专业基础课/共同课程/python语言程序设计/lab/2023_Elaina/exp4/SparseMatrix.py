"""
SparseMatrix.py
author: Elaina
date: 2023/11/14
description: use Python dictionaries to represent sparse matrices and deal with computation of sparse matrices.
"""

def toSparseMatrix(sparsemat):
    m = dict()
    for i in range(0, len(sparsemat), 1):
        for j in range(0, len(sparsemat[i]), 1):
            if sparsemat[i][j] != 0:
                m[(i,j)] = float(sparsemat[i][j])
    return m

def judge(sparsemat1, sparsemat2, size):
    ls1 = list(sparsemat1.keys())
    ls2 = list(sparsemat2.keys())
    mat_size = 0
    for i in ls1:
        for j in i:
            mat_size = max(mat_size, j)
    for i in ls2:
        for j in i:
            mat_size = max(mat_size, j)
    if size <= mat_size:
        print("matrix size is not valid!")
        raise Exception("matrix size is not valid!")
    return mat_size

def AddSparseMatrix(sparsemat1, sparsemat2, size):
    judge(sparsemat1, sparsemat2, size)
    m = {}
    for key, val in sparsemat1.items():
        if key not in m:
            m[key] = float(val)
        else:
            m[key] += float(val)
    for key, val in sparsemat2.items():
        if key not in m:
            m[key] = float(val)
        else:
            m[key] += float(val)
    return m

def SubSparseMatrix(sparsemat1, sparsemat2, size):
    judge(sparsemat1, sparsemat2, size)
    m = {}
    for key, val in sparsemat1.items():
        if key not in m:
            m[key] = float(val)
        else:
            m[key] += float(val)
    for key, val in sparsemat2.items():
        if key not in m:
            m[key] = -float(val)
        else:
            m[key] -= float(val)
    return m

def fill(sparsemat, size):
    matrix = [[0 for i in range(size)] for j in range(size)]
    for pos, val in sparsemat.items():
        matrix[pos[0]][pos[1]] = val
    return matrix

def RowIsAllZero(sparsemat, size):
    res = []
    for i in range(0, size, 1):
        res.append(i)
    for pos in sparsemat:
        if pos[0] in res:
            res.remove(pos[0])
    return res

def ColIsAllZero(sparsemat, size):
    res = []
    for i in range(0, size, 1):
        res.append(i)
    for pos in sparsemat:
        if pos[1] in res:
            res.remove(pos[1])
    return res

def mul(matrix1, matrix2, size, col, row):
    ans = 0
    for i in range(0, size, 1):
        ans += (matrix1[row][i] * matrix2[i][col])
    return ans

def MulSparseMatrix(sparsemat1, sparsemat2, size):
    m = {}
    matrix1 = fill(sparsemat1, size)
    matrix2 = fill(sparsemat2, size)
    mat1_zero_row = RowIsAllZero(sparsemat1, size)
    mat2_zero_col = ColIsAllZero(sparsemat2, size)
    print(mat1_zero_row,mat2_zero_col)
    for row in range(0, size, 1):
        for col in range(0, size, 1):
            if (row in mat1_zero_row) or (col in mat2_zero_col):
                continue
            else:
                pos = (row, col)
                num = mul(matrix1, matrix2, size, col, row)
                if num != 0:
                    m[pos] = float(num)
    return m

# # Example 1
# spmatrix1 = toSparseMatrix([[0,0,1,0],[1,0,0,0]])
# print(spmatrix1.items())

# Example 2
# sparsemat1 = {
# (0,2):1,
# (1,0):1
# }
# sparsemat2 = {
# (0,2):1,
# (1,0):1
# }
# spmat = AddSparseMatrix(sparsemat1, sparsemat2, 3)
# print(spmat.items())
# # the following statement will throw a exception...
# spmat = AddSparseMatrix(sparsemat1, sparsemat2, 2)
# print(spmat.items())

# # Example 3
# sparsemat1 = {
# (0,2):1,
# (1,0):1
# }
# sparsemat2 = {
# (0,1):1,
# (1,0):1
# }
# spmat = SubSparseMatrix(sparsemat1, sparsemat2, 3)
# print(spmat.items())

# # Example 4
# sparsemat1 = {
# (0,2):1,
# (1,0):1
# }
# sparsemat2 = {
# (0,1):1,
# (1,0):1,
# (3,0):1,
# (3,1):1
# }
# spmat = MulSparseMatrix(sparsemat1, sparsemat2, 4)
# print(spmat.items())

# # Example 5
# sparsemat1 = {
# (0,2):1,
# (1,0):1,
# (2,2):1,
# (3,0):1
# }
# sparsemat2 = {
# (0,1):1,
# (1,0):1,
# (2,2):1,
# (3,0):1,
# (3,1):1
# }
# spmat = MulSparseMatrix(sparsemat1, sparsemat2, 4)
# print(spmat.items())