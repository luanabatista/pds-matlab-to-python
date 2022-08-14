import numpy as np
import matplotlib.pyplot as plt
from numpy import fft
from scipy import signal as sigs

# Ilustração do uso da função firpm que executa o algoritmo de Parks-McClellan para encontrar coeficientes de filtro FIR.
# coeficientes para filtro passa-faixa:
#  f = [0 0.4 0.44 0.56 0.6 1];
#  a = [0 0 1 1 0 0];
# coeficientes para filtro passa-baixas:
f = np.array([0, 0.4, 0.5, 1]);
m = np.array([1, 0]);
coef = sigs.remez(33,bands=f,desired=m, fs=2);
w, h = sigs.freqz(coef);
angles = np.unwrap(np.angle(h))

plt.subplot(2,1,1); plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.subplot(2,1,2); plt.plot(w, angles*20, 'g')
plt.show()
