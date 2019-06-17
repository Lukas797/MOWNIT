import numpy as np
import math

#zadanie1

print(np.float32(1/3))
print(np.float64(1/3))
print(np.float64(np.float32(1/3)))

#zadanie2

import matplotlib.pyplot as mtp
x = np.linspace(1.0, 1000, 1000)
y =  np.nextafter(x, x+1)-x

mtp.plot(x, y, 'x')
mtp.show()

#zadanie4

a = 1/10**16
b = 1/(10**16 + 4)

r1 = a**2 - b**2  #niestabilny numerycznie
#dziala źle, ponieważ algorytm jest bardzo podatny na zaburzenia danych, wynika to z faktu, że zaburzenia są zależne od danych,
#im bliżej siebie są dane a i b, tym zaburzenie bedzie wieksze

r2 = (a-b)*(a+b)  #stabilny numerycznie
#dziala dobrze, ponieważ po przeprowadzeniu dowodu okazuje sie, że blad nigdy nie przekoczy granicy 3|maxi Ei|, gdzie Ei to bledy wynikajace
#z zaburzenia danych i dzialan uzytych w algorytmie
print(r1)
print(r2)









