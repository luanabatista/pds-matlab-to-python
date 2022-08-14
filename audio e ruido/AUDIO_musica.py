import numpy as np
import matplotlib.pyplot as plt
from numpy import fft
from scipy import signal as sigs
import soundfile as sf

def ctranspose(arr: np.ndarray) -> np.ndarray:
    # Explanation of the math involved:
    # x      == Real(X) + j*Imag(X)
    # conj_x == Real(X) - j*Imag(X)
    # conj_x == Real(X) + j*Imag(X) - 2j*Imag(X) == x - 2j*Imag(X)
    tmp = arr.transpose()
    return tmp - 2j*tmp.imag

#Importar o audio
[a, fs]= sf.read('ATOA_musica_ruidosa_teste5.wav');# Se tivesse duas colunas podemos somar as duas e multipllicar 0.5
d=len(a)/fs;
b=len(a); #comprimento do audio

#Graficar o formato da onda
t=np.linspace(0,d,b);
plt.figure
plt.plot(t,a)
plt.title('Formato de onda')
plt.xlabel('tempo')
plt.ylabel('amplitude')

#Funcao da frequencia
fdt=fft.fft(a);
fdtc=fft.fftshift(fft.fft(a));
freq=np.linspace(-fs/2,fs/2,len(fdt));
mag=abs(fdt);
magc=abs(fdtc);
fase=np.angle(fdt);
fasec=np.angle(fdtc);
plt.figure
plt.plot(freq,mag)
plt.title('Magnitude fft');
plt.xlabel('Hz');
plt.ylabel('amplitude')
plt.figure
plt.plot(freq,(magc/max(magc)));#normalizar
plt.title('Magnitude fftshift');
plt.xlabel('Hz');
plt.ylabel('amplitude')
plt.figure
plt.plot (freq,fasec)
plt.title('fase');
plt.xlabel('Hz');
plt.ylabel('graus');
##

#filtro pasabajas

#Exemplo 1b: passa-baixas (frequencia nominal considerando Fs=20k)
fc = 1000;
Fs1 = 8e3;
ordem=32;
resol_plot_freq = 1000;
coef = sigs.firwin(ordem, (fc/(Fs1/2)));
[H , freq1] = sigs.freqz(coef,1,resol_plot_freq, Fs1);
plt.figure
plt.plot(freq1,abs(H));
plt.title('Magnitude filtro');
plt.xlabel('Hz');
plt.ylabel('graus');
#graficar filtro e o sinal de entrada

#filtra
coeficientes=ctranspose(H)


saida = sigs.lfilter(coeficientes,1,a);
#sound(a)
#pause (3)
#sound (saida)
#grafico frequencia filtrado

saidafft=fft.fft(saida)
magfil=abs(saidafft)
#sound (magfil)
plt.figure
plt.plot(freq,(magfil/max(magfil)));#normalizar
plt.title('Magnitude sinal filtrado');
plt.xlabel('Hz');
plt.ylabel('amplitude')

plt.show()
erro
