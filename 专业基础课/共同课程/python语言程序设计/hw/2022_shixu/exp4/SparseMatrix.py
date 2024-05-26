"""
SparseMatrix.py
author:张辰旭
date:2023.04.11
description:about SparseMatrix
"""
def ToSparseMatrix(sparsemat):
    SM = {}
    for i in range(len(sparsemat)):
        for j in range(len(sparsemat[i])):
            if sparsemat[i][j] != 0:
                SM[(i, j)] = sparsemat[i][j]
    return SM


def AddSparseMatrix(sparsemat1, sparsemat2, size):
    if any(max(n) >= size for n in sparsemat1.keys()) or any(max(n) >= size for n in sparsemat2.keys()):
        print("matrix size is not valid!")
        return None
    result = {}
    for key in sparsemat1:
        if key in sparsemat2:
            result[key] = sparsemat1[key] + sparsemat2[key]
        else:
            result[key] = sparsemat1[key]
    for key in sparsemat2:
        if key not in result:
            result[key] = sparsemat2[key]

    return result

def SubSparseMatrix(sparsemat1, sparsemat2, size):
    if any(max(n) >= size for n in sparsemat1.keys()) or any(max(n) >= size for n in sparsemat2.keys()):
        print("matrix size is not valid!")
        return None
    result = {}
    for key in sparsemat1:
        if key in sparsemat2:
            result[key] = sparsemat1[key] - sparsemat2[key]
        else:
            result[key] = sparsemat1[key]
    for key in sparsemat2:
        if key not in result:
            result[key] = -sparsemat2[key]
    return result

def MulSparseMatrix(sparsemat1, sparsemat2, size):
    if any(max(n) >= size for n in sparsemat1.keys()) or any(max(n) >= size for n in sparsemat2.keys()):
        print("matrix size is not valid!")
        return None
    result = {}
    for i in range(size):
        for j in range(size):
            dot_product = 0
            for k in range(size):
                if (i, k) in sparsemat1 and (k, j) in sparsemat2:
                    dot_product += sparsemat1[(i, k)] * sparsemat2[(k, j)]
            if dot_product != 0:
                result[(i, j)] = dot_product
    return result


print("#test ToSparseMatrix")
spmatrix1 = ToSparseMatrix([[0,0,1,0],[1,0,0,0]])
print(spmatrix1)
print("#==================================")

print("#test AddSparseMatrix_1")
sparsemat1 = {(0,2):1,(1,0):1}
sparsemat2 = {(0,2):1,(1,0):1}
spmat = AddSparseMatrix(sparsemat1, sparsemat2, 3)
print(spmat)
print("#test AddSparseMatrix_2")
sparsemat1 = {(0,2):1,(1,0):1}
sparsemat2 = {(0,2):1,(1,0):1}
spmat = AddSparseMatrix(sparsemat1, sparsemat2, 1)
print(spmat)
print("#==================================")


print("#test SubSparseMatrix")
sparsemat1 = {(0,2):1,(1,0):1}
sparsemat2 = {(0,1):1,(1,0):1}
spmat = SubSparseMatrix(sparsemat1, sparsemat2, 3)
print(spmat)
print("#==================================")

print("#test MulSparseMatrix")
sparsemat1 = {(0,2):1,(1,0):1}
sparsemat2 = {(0,1):1,(1,0):1,(3,0):1,(3,1):1}
spmat = MulSparseMatrix(sparsemat1, sparsemat2, 4)
print(spmat)
print("#==================================")