# Implementação de um filtro FIR dados seus coeficientes
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft

def ctranspose(arr: np.ndarray) -> np.ndarray:
    # Explanation of the math involved:
    # x      == Real(X) + j*Imag(X)
    # conj_x == Real(X) - j*Imag(X)
    # conj_x == Real(X) + j*Imag(X) - 2j*Imag(X) == x - 2j*Imag(X)
    tmp = arr.transpose()
    return tmp - 2j*tmp.imag

h=np.array([-0.0010, -0.0007, 0.0004, 0.0015, 0.0017, -0.0000, -0.0028, -0.0042, -0.0017, 0.0040, 0.0085, 0.0061, -0.0039, -0.0144, -0.0147, 0.0000, 0.0211, 0.0298, 0.0117, -0.0273, -0.0581, -0.0442, 0.0318, 0.1493, 0.2568, 0.3003, 0.2568, 0.1493, 0.0318, -0.0442, -0.0581, -0.0273, 0.0117, 0.0298, 0.0211, 0.0000, -0.0147, -0.0144, -0.0039, 0.0061, 0.0085, 0.0040, -0.0017, -0.0042, -0.0028, -0.0000, 0.0017, 0.0015, 0.0004, -0.0007, -0.0010])
n_h = np.arange(0, 51)
## PARTE 1: Gera um sinal analógico (entrada_analogica) e sua versão discretizada
# (entrada_discretizada)
Fs = 20000; # taxa de amostragem: 20mil amostras/seg
t = np.arange(0,0.02,(1/Fs)); # amostragem de 0,02seg  0:(1/Fs):0.02	arange(0,1.02,(1/Fs))
N = max(t)/(1/Fs);
n = np.arange(0, N+1) # quantidade de amostras da entrada para filtrar
#entrada_analogica = np.sin(2*np.pi* 200*t) + np.sin(2*np.pi*25*t) + np.sin(2*np.pi* 5000*t) + np.sin(2*np.pi*9000*t);
entrada_discretizada = np.sin(2*np.pi*200*n/Fs) + np.sin(2*np.pi*25*n/Fs) + np.sin(2*np.pi*5000*n/Fs) + np.sin(2*np.pi*9000*n/Fs);

## PARTE 2: convolui entrada com h
saida = np.convolve(entrada_discretizada, ctranspose(h));

## PARTE 3: PLOTA RESULTADOS
# calcula espectro entrada
fft_sinal_entrada = fft.fft(entrada_discretizada)/N;
f_entrada = n*(Fs/N);

# calcula espectro saida
N3 = np.size(saida);
fft_sinal_saida = fft.fft(saida)/N3;
n3 = np.arange(0, np.size(fft_sinal_saida))
f_saida = n3*(Fs/N3);

# calcula espectro filtro
fft_resp_filtro = fft.fft(h);
n4 = np.arange(0, np.size(fft_resp_filtro))
N4 = np.size(n4);
f_h = n4*(Fs/N4);

# plota espectros
plt.subplot(3,1,1); plt.stem(n_h,h); plt.xlabel('n'); plt.title('Coef. filtro');
plt.subplot(3,1,2); plt.plot(f_entrada[0:int(N/2)], abs(fft_sinal_entrada[0:int(N/2)]), label='entrada');
plt.plot(f_saida[0:int(N3/2)], abs(fft_sinal_saida[0:int(N3/2)]),'r', label='saída');
plt.plot(f_h[0:int(N4/2)], abs(fft_resp_filtro[0:int(N4/2)]),'g', label='resp. impulsiva');
plt.legend();
plt.xlabel('Freq (Hz)');
plt.title('Espectros dos sinais e filtro')

# plota sinais
plt.subplot(3,1,3); plt.plot(n, entrada_discretizada, label='entrada');
plt.plot(n3, saida,'r', label='saída');
plt.legend();
plt.xlabel('n');
plt.title('Sinais discretos do filtro');
plt.show()