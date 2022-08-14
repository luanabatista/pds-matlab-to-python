import numpy as np
import matplotlib.pyplot as plt
from numpy import fft

## gera um sinal "sintetico" com 3 componentes de frequencia
Fs = 1000; #taxa de aquisicao do sinal
ts = 1/Fs;
N = 1000; #numero amostras de amostras analisadas
t = (np.arange(0, N))*ts;
sinal = 0.6*np.sin(2*np.pi*50*t) + 2*np.sin(2*np.pi*120*t) + 0.3*np.sin(2*np.pi*400*t);
ruido = 0.4*np.random.randn(np.size(t));
## calcula a DFT usando a funcao fft
y = fft.fft(sinal+ruido);
y = y/N; #se desejar pode-se dividir por N para "acomodar" os calculos
## calcular o eixo das frequencias
m = np.arange(0, N)
f = m*Fs/N;
y = y[0:int(N/2)] #pegando so a primeira metade ja que a outra é copia
f = f[0:int(N/2)] #pegando so a primeira metade ja que a outra é copia
## calcular a potencia do espectro em db
magnitude = abs(y);
fase = np.angle(y);
f_ref = max(magnitude); #escolhe o maior valor para ser a referencia para normalizacao
y_db = 20*np.log10(magnitude/f_ref); #lembre que, por exemplo 0db = 1 unidade
## plotar
plt.subplot (3,1,1); plt.plot(f ,magnitude); plt.title('magnitude espectro'); plt.xlabel('freq(Hz)');
plt.ylabel('Amplitude');
plt.subplot (3,1,2); plt.plot(f ,y_db); plt.title('potencia espectro');
plt.subplot (3,1,3); plt.plot(f ,fase); plt.title('fase');
plt.show()