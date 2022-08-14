# diferença entre resolução espectral e densidade espectral
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft
n = np.arange(0, 100)
Fs = 100
x = np.cos(0.48*np.pi*n) + np.cos(0.52*np.pi*n)
## calcula DFT com N=10 e plota
n1 = np.arange(0, 10)
sinal1 = x[0:10]
Y1 = fft.fft(sinal1, 10)
magY1 = abs(Y1[0:6])
N1 = 5
m1= np.arange(0, 6)
f1= m1*Fs/N1
plt.subplot(2,3,1); plt.stem(sinal1); plt.xlabel('n'); plt.title('N=10')
plt.subplot(2,3,4); plt.stem(f1, magY1); plt.xlabel('freq(Hz)');
## calc DFT com N=10+90 zeros e subplota (melhor resol espectro)
aux = np.zeros((1,90))
sinal2 = np.concatenate((x[0:10], aux[0]))   #preencheu sinal que essencialmente eh o mesmo
Y2 = fft.fft(sinal2, 100)
magY2 = abs(Y2[0:50])
N2 = 50
m2= np.arange(1, 51)
f2= m2*Fs/N2
plt.subplot(2,3,2); plt.stem(sinal2); plt.xlabel('n'); plt.title('N=10+90 zeros com boa resol. espec.')
plt.subplot(2,3,5); plt.stem(f2, magY2); plt.xlabel('freq(Hz)');
## calc DFT com N=100
sinal3 = x[0:100]
Y3 = fft.fft(sinal3, 100)
magY3 = abs(Y3[0:50])
N3 = 50;
m3= np.arange(1, 51)
f3= m3*Fs/N3;
plt.subplot(2,3,3); plt.stem(sinal3); plt.xlabel('n'); plt.title('N=100 com boa densid. espec.')
plt.subplot(2,3,6); plt.stem(f3, magY3); plt.xlabel('freq(Hz)');
plt.show()