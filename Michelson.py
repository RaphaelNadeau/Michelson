import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from numpy.fft import *

""" Ce script genere des interferogrammes tels qu'obtenus avec un interferometre
de Michelson dans le but d'etudier la transformée de Fourier et de comprendre 
comment la resolution spectrale est déterminée.
"""


def readVectorsFromFile(filename):
    x = np.loadtxt(filename, usecols=(1))
    # print(type(x))
    x = 2 * x * 1.1
    y = np.loadtxt(filename, usecols=(2))
    return (x, y)


def fourierTransformInterferogram(x, y):
    """ A partir du tableau de valeurs Y correspondant a l'abscisse X,
    la transformée de Fourier est calculée et l'axes des fréquences (f en
    µm^-1) et des wavelengths (1/f en microns) est retournée.
    Le spectre est un ensemble de valeurs complexes pour lesquelles l'amplitude
    et la phase sont pertinentes: l'ordre des valeurs commence par la valeur DC (0)
    et monte jusqu'a f_max=1/2/∆x par resolution de ∆f = 1/N/∆x. A partir de la
    (N/2) ieme valeur, la frequence est negative jusqu'a -∆f dans la N-1 case.
    Voir
    https://github.com/dccote/Enseignement/blob/master/HOWTO/HOWTO-Transformes%20de%20Fourier%20discretes.pdf
    """
    spectrum = fft(y)
    dx = x[1] - x[0]  # on obtient dx, on suppose equidistant
    N = len(x)  # on obtient N directement des données
    frequencies = fftfreq(N, dx)  # Cette fonction est fournie par numpy
    # print(frequencies)
    wavelengths = 1 / frequencies  # Les fréquences en µm^-1 sont moins utiles que lambda en µm
    return (wavelengths, frequencies, spectrum)


def plotCombinedFigures(x, y, w, s, title="", left=400, right=800):
    """"
    On met l'interferogramme et le spectre sur la meme page.
    """
    fig, (axes, axesFFT) = plt.subplots(2, 1, figsize=(10, 7))
    axes.plot(x, y, '-')
    axes.set_title("Interferogramme")
    axesFFT.plot(w * 1000, abs(s), '-')
    axesFFT.set_xlim(left=left, right=right)
    axesFFT.set_xlabel("Longueur d'onde [nm]")
    axesFFT.set_title(title)
    plt.show()


if __name__ == '__main__':
    path = r'D:\Desktop\Université Raph\Hiver 2020\Optique expérimentale\Michelson'

    # laser He-Ne
    (x, y) = readVectorsFromFile(path + r'\Interférogramme\HeNeSem2.jpg')  # en microns
    (w, f, s) = fourierTransformInterferogram(x, y)
    df = f[1] - f[0]
    dl = 0.6328 * 0.6328 * df * 1000  # x 1000 pour nm
    plotCombinedFigures(x, y, w, s, left=500 - 5 * dl, right=1000 - 5 * dl,
                        title="Spectre He-Ne, resolution resolution {0:0.2f} nm".format(dl))

    # Spectre de lumiere blanche
    # Resolution ∆f = 1/(20000 µm * 20000)
    # Resolution @ 500 nm : ∆lambda = 500^2 * ∆f
    (x, y) = readVectorsFromFile(path + r'\Interférogramme\blanchehalo2.jpg')  # en microns
    (w, f, s) = fourierTransformInterferogram(x, y)
    df = f[1] - f[0]
    dl = 0.500 * 0.500 * df * 1000  # resolution autour de 0.500 µm en nm
    plotCombinedFigures(x, y, w, s, left=0, right=2000,
                        title="Spectre lumiere blanche, resolution {0:0.2f} nm".format(dl))

    # spectre de la lumière au sodium pour la longueur d'onde
    (x, y) = readVectorsFromFile(path + r'\Interférogramme\Na2.txt')  # en microns
    (w, f, s) = fourierTransformInterferogram(x, y)
    df = f[1] - f[0]
    dl = 0.580 * 0.580 * df * 1000  # resolution autour de 0.500 µm en nm
    plotCombinedFigures(x, y, w, s, left=0, right=2000,
                        title="Spectre lampe au Sodium, resolution {0:f} nm".format(dl))

    # spectre de la lumière au sodium pour l'enveloppe
    (x, y) = readVectorsFromFile(path + r'\Interférogramme\Na3.jpg')  # en microns
    (w, f, s) = fourierTransformInterferogram(x, y)
    df = f[1] - f[0]
    dl = 0.580 * 0.580 * df * 1000  # resolution autour de 0.500 µm en nm
    plotCombinedFigures(x, y, w, s, left=0, right=2000,
                        title="Spectre enveloppe lampe Sodium, resolution {0:f} nm".format(dl))
