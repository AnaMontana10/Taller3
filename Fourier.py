import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq


signal= np.genfromtxt('signal.dat', delimiter= ',')
incompleto= np.genfromtxt('incompletos.dat')
c1=[:,0]
c2=[:,1]

plt.figure()
plt.imshow(signal)
plt.show()
plt.savefig("MontanaAna_signal.pdf")