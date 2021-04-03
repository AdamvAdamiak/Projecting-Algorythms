import numpy as np
from math import sin
from matplotlib import pyplot as plt
from fourier_transformation import fft, define_data
from scipy import ifft


def remove_frequency(data, freq=0.9):
    for i in range(len(data)):
        if data[i] > freq:
            data[i] = 0
    return data


def show_plot():
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data = define_data()
    hamming = np.hamming(len(data))

    data = data * hamming

    data = fft(data)
    plt.plot(data, color='orange', label='transformed data')

    data = remove_frequency(data)
    plt.plot(data, color='black', label='removed frequency')

    data = ifft(data)
    plt.plot(data, color='red', label='removed frequency, ifft')

    show_plot()
