# FILTRO USANDO FUNÇÃO FIR1 - Calculos coeficientes filtro FIR usando função FIR1
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft
from scipy import signal as sigs

ordem = 50;
resol_plot_freq = 512;
# Exemplo 1a: passa-baixas (frequencia normalizada)

#b = fir1(n,Wn)
#scipy.signal.firwin(numtaps, cutoff, width=None, window='hamming', pass_zero=True, scale=True, nyq=None, fs=None)[source]

coef = sigs.firwin(ordem, 0.3);
# Exemplo 1b: passa-baixas (frequencia nominal considerando Fs=20k)
fc = 3000;
Fs = 20e3;
coef = sigs.firwin(ordem, fc/(Fs/2));
[H , freq] = sigs.freqz(coef,1,resol_plot_freq, 20e3);
print(coef)
plt.plot(freq,abs(H));
plt.show()
erro
#  # Exemplo 2: passa-altas
#  coef = fir1(ordem, 0.4,'high');
#  freqz(coef,1,resol_plot_freq)
#  # Exemplo 3: passa-altas com janela de Hanning
#  coef = fir1(ordem, 0.6, 'high', hann(ordem+1));
#  freqz(coef,1,resol_plot_freq)
#  # Exemplo 4: passabanda
#  coef = fir1(ordem, [0.3 0.5]);
#  freqz(coef,1,resol_plot_freq)
#  # Exemplo 5: rejeita-banda
#  coef = fir1(ordem, [0.3 0.7], 'stop');
#  freqz(coef,1,resol_plot_freq)