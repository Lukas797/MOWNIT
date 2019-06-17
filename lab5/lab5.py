import numpy as np
#zadanie 1 funkcja liczaca blad sredniokwadratowy
from typing import List

def rmse(x: List[float], y: List[float]) -> float:
    whole = 0
    for vx , vy in zip(x, y):
        whole += (vx - vy) * (vx - vy)
    return whole


#zadanie 2 regresja liniowa

from typing import Tuple

def linear_regression(lx: List[float], ly: List[float]) -> Tuple[float, float]:
    length = len(lx)
    mean_x = np.mean(lx)
    mean_y = np.mean(ly)
    tmp1 = x * y
    tmp2 = x * x
    mean_xy = mean_x * mean_y
    mean_xx = mean_x * mean_x
    xy = np.sum(tmp1 - mean_xy)
    xx = np.sum(tmp2 - mean_xx)

    res1 = xy/xx
    res2 = mean_y - res1 * mean_x

    return res1, res2


#zadanie 3 klasa enkapsulujaca model regresji liniowej

from typing import List, Tuple, Optional

class LinReg():
    def __init__(self):
        self.__coeffs = None

    def fit(self, x: List[float], y: List[float]) -> None:
        length = len(lx)
        mean_x = np.mean(lx)
        mean_y = np.mean(ly)
        tmp1 = x * y
        tmp2 = x * x
        mean1 = mean_x * mean_y
        mean2 = mean_x * mean_x
        mean_xy = np.sum(tmp1 - mean1)
        mean_xx = np.sum(tmp2 - mean2)

        res1 = mean_xy/mean_xx
        res2 = mean_y - res1 * mean_x

        self.coeffs = (res1, res2)

    def predict(self, lx: List[float]) -> List[float]:
        (a, b) = self.__coeffs
        return [a * i + b for i in lx]

    def coeffs(self) -> Tuple[float, float]:
        if self.coeffs is None:
            raise Exception('First call fit method.')
        return self.__coeffs

#zadanie 4 testowanie klasy

import csv
objlr = LinReg()
lx = []
ly = []
with open('dane.csv', newline='') as file:
    k = csv.reader(file, delimiter =',')
    for r in k:
        lx.append(float(r[0]))
        ly.append(float(r[1]))

objlr.fit(lx, ly)
l = list(range(1, 100, 10))
p = objlr.predict(l)
for(x, y) in zip(l, p):
    print(str(x) + ": " + str(y))

import matplotlib.pyplot as plt
import numpy as np

def plot_data(xs: List[float], ys: List[float]) -> None:
    objlr.fit(xs, ys)
    def fun(x):
        (a, b) = objlr.coeffs
        return a * x + b
    ls = np.linspace(min(xs), max(xs), 1000)
    plt.plot(xs,ys, 'ro')
    plt.plot(ls, fun(ls))
    plt.show()

plot_data(xs, ys)


