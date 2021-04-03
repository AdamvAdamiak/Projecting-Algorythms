import numpy as np
from math import sin
from matplotlib import pyplot as plt


def dft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def fft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    if N % 2 > 0:
        raise ValueError("must be a power of 2")
    elif N <= 2:
        return dft(x)
    else:
        X_even = fft(x[::2])
        X_odd = fft(x[1::2])
        terms = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + terms[:int(N/2)] * X_odd,
                               X_even + terms[int(N/2):] * X_odd])


def signal(t):
    return 5*sin(t) + 3*sin(2*t) + 5*sin(5*t)


def define_data():
    data = []
    for i in range(128):
        data.append(signal(i))
    return np.array(data)


if __name__ == '__main__':
    plt.plot(define_data(), color='orange', label='Data')
    transformed = fft(define_data())
    plt.plot(transformed, color='red', label='Fast Fourier Transformation')
    plt.legend()
    plt.show()
