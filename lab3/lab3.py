import numpy as np

#zadanie 1a Gauss bez pivotingu

import numpy as np

def gauss(A, B):
    length = len(A)
    A = np.copy(A)
    B = np.copy(B)

    for i in range(length):
        for j in range(length):
            if i != j:
                s = A[j, i]/A[i, i]
                A[j] -= A[i] * s
                B[j] -= B[i] * s
    for i in tange(length):
        B[i] /= A[i, i]

    return B

# zadanie 1b Gauss z pivotingiem

def pivoting(A, B):
    length = len(A)
    A = np.copy(A)
    B = np.copy(B)

    for i in range(length - 1):
        maximum = abs(A[i:,i]).argmax() + i
        if maximum != i:
            A[[i, maximum]] = A[[maximum, i]]
            B[[i, maximum]] = B[[maximum, i]]

        for r in range(i+1, n):
            s = A[r, i]/A[i,i]
            A[r, i:] = A[r, i:] - s*A[i, i:]
            B[r] = B[r] - s*B[i]

    for i in range(length - 1, -1, -1):
        B[i] = (B[i] - np.dot(A[i,i+1:], B[i+1:])).A[i,i]]

    return B

# zadanie 2 algorytm faktoryzacji LU

def multiply(M, N):
    return [[sum(m * n for m,n in zip(rm, cln)) for cln in np.transpoe(N)] for rm in M]

def pivot(M):
    length = len(M)
    id = np.identity(length)
    for j in range(length):
        r = max(range(j, length), key =(lambda x:abs(M[x][j])))
        if j != r:
            id[j], id[r] = id[r], id[j]
    return id

def lu(A):
    length = len(A)

    C = np.zeros((n,n))
    D = np.zeros((n,n))

    Pivot = pivot(A)
    Pivot1 = multiply(Pivot, A)

    for i in range(length):
        C[i][i] = 1.0
        for j in range(i+1):
            s = sum(D[k][i] * C[j][k] for k in range(j))
            D[j][i] = Pivot1[j][i] - s
        for j in range(i, n):
            s = sum(D[k][i] * C[j][k] for k in range(i))
            C[j][i] = (Pivot1[j][i] - s) / D[i][i]

    return (Pivot, C, D)


# zadanie 3 funkcja sprawdzjaca (symetrycznosc, dodatnio okreslona)

def check(A):
    return np.all(np.linalg.eigvals(A) > 0)

# zadanie 4 faktoryzacja Cholesky'ego

def cholesky(A):
    length = len(A)
    C = np.zeros((n, n))

    for i in range(length):
        for j in range(i+1):
            tmp = sum(C[i][k] * C[i][k] for k in range(j))
            if(i == j):
                C[i][j] = np.sqrt(A[i][i] - sum)
            else:
                C[i][j] = (1.0 / C[j][j] * (A[i][j] - tmp))
    return C












