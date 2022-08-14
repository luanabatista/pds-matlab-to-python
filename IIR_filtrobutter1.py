import numpy as np
import matplotlib.pyplot as plt
from numpy import fft
from scipy import signal as sigs

fs=8000;
wp1= 500;
ws1= 750;

#normaliza em funcao da freq Nysquest = Fs/2.    
wp1= wp1/(fs/2);
ws1= ws1/(fs/2);
atenuacao_filtro=20;

[ord, wn]=sigs.buttord(wp1,ws1, 1, atenuacao_filtro);
[num, dem]= sigs.butter(ord,wn,btype='low');
[freq3, H] = sigs.freqz(num,dem,worN=512, fs=fs);

print(H)
plt.plot(freq3,abs(H))
plt.title('Magnitude filtro');
plt.xlabel('Hz');
plt.ylabel('graus');
plt.show()