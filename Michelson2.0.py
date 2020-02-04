import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from numpy.fft import *


def readVectorsFromFile(filename):
    x = np.loadtxt(filename, usecols=(0))
    # print(type(x))
    # x = 2 * x *1.1
    y = np.loadtxt(filename, usecols=(1))
    return (x, y)


if __name__ == '__main__':
    path = r'D:\Desktop\Université Raph\Hiver 2020\Optique expérimentale\Michelson'


    (x, y) = readVectorsFromFile(path + r'\Spectre\blanchehalospectre.txt')
    plt.plot(x, y)
    plt.show()

    (x, y) = readVectorsFromFile(path + r'\Spectre\HeNespectre.txt')
    plt.plot(x, y)
    plt.show()

    (x, y) = readVectorsFromFile(path + r'\Spectre\hg.txt')
    plt.plot(x, y)
    plt.show()

    (x, y) = readVectorsFromFile(path + r'\Spectre\spectreNa.txt')
    plt.plot(x, y)
    plt.show()

    (x, y) = readVectorsFromFile(path + r'\Spectre\spectreNa2.txt')
    plt.plot(x, y)
    plt.show()
