#zadanie 1 metoda Jacobiego

import numpy as np

def jacobi(A: np.matrix, B :np.matrix, len: int = 50) -> np.matrix:
    xs = np.zeros((A.shape[0], 1))

    Diag = np.diag(A)
    R = A - np.diagflat(Diag)
    Diag = Diag.reshape((A.shape[0], 1))

    for i in range(len):
        xs = (B - np.dot(R, xs)) / Diag
    return xs

#zadanie 2 metoda Gaussa-Seidla

def gauss_seidel(A: np.matrix, B: np.matrix, len: int = 50) -> np.matrix:
    xs = np.zeros((A.shape[0], 1))
    C = np.tril(A)
    D = A - C
    for i in range(len):
        xs = np.dot(np.linalg.inv(C), B - np.dot(C, xs))
    return xs

#zadanie 3 metoda SOR

def sor(A: np.matrix, B: np.matrix, len: int = 50, f: int = 1) -> np.matrix:
    xs = np.zeros((A.shape[0], 1))

    C = np.tril(A, -1)
    D = np.triu(A, 1)
    E = np.diagflat(np.diagonal(A))

    for i in range(len):
        xs = np.dot(np.linalg.inv(E + f * C), f * B - np.dot(f * D + (f - 1) * E, xs ))

#zadanie 4 porowanie tempa zbiegania

def way_dist(A: np.matrix, B: np.matrix) -> int:
    whole = 0
    for i in range(A.shape[0]):
        whole += (A.item(i, 0)) - B.item((i, 0)) ** 2
    return whole


# do zbadania tempa zbiegania i poprawnosci algorytmow mozna uzyc danych

G = np.matrix([[5., -2.,3.,1.],
               [-1.,4.,5.,1.],
                [4.,2.,-1.,2.],
                [8.,2.,3.,-1.]])
H = np.matrix([1., 12., -5., 10.]).transpose()
