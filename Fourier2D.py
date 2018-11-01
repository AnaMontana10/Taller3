import numpy as np
from scipy import misc
from scipy.fftpack import fft, fftfreq, fft2



imagen = misc.imread('arbol.png')

f1= fftpack.fft2(imagen)