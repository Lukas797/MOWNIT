import numpy as np

#zadanie1 dyskretna transformata Fouriera

def DFT(x):
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n/N)
    return np.dot(M, x)


#sprawdzanie poprawnosci
x = np.random.random(2048)
print(np.allclose(DFT(x), np.fft.fft(x)))

#zadanie2 szybka transformata Fouriera

def FFT(x):
    N = x.shape[0]
    if N <= 32:
        return DFT(x)
    else:
        even = FFT(x[::2])
        odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N)/N)
        return np.concatenate([even + factor[:N // 2] * odd,
                              even + factor[N // 2:] * odd])

#sprawdzanie poprawnosci
x = np.random.random(1024)
print(np.allclose(FFT(x), np.fft.fft(x)))

#zadanie3 analiza szeregu czasowego

import pandas as pd

data = pd.read_csv('water-consumption-in-the-new-york-city.csv')
print(data.dtypes)

print(data)

#import matplotlib.pyplot as plt # do wykresów
#import numpy as np              # do macierzy
#from scipy import fftpack       # do FFT

#X = fftpack.fft(dataset)
#f_s = 1  # godzinowo
#freqs = fftpack.fftfreq(len(dataset)) * f_s # czętotliwości
#fig, ax = plt.subplots()

#ax.stem(freqs[:40], np.abs(X)[:40])
#ax.set_xlabel('Frequency in hits/hour')
#ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
#ax.set_ylim(-1, 200)
#plt.show()


