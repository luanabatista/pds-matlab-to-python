import numpy as np
import matplotlib.pyplot as plt
from numpy import concatenate, fft
from scipy.io.wavfile import write
from scipy import signal as sigs
import soundfile as sf
import wave

dados = wave.open('ATOA_musica_ruidosa_teste5.wav', 'r')
print(dados.getparams())
## Parte 1: gera ruido e plota seu espectro    
#dados = importdata('ATOA_musica_ruidosa_teste5.wav');
musica_original = dados;
Fs = dados._nframes;
espectro_original = abs(fft.fft(musica_original));
N = len(musica_original);
m = np.arange(0, N)
freq_espectro_original = m*Fs/N;
espectro_original = espectro_original[0:round(N/2)];
freq_espectro_original = freq_espectro_original[0:round(N/2)];   
plt.subplot(4,1,1); plt.plot(musica_original); plt.title('musica original no tempo');
plt.subplot(4,1,2); plt.plot(freq_espectro_original, espectro_original); plt.title('Espectro sinal original'); 
    
## Parte 1: projeta filtro para tirar ruido    
inicio = input('Digite a primeira frequencia a ser filtrada: ');
fim = input('Digite a ultima frequencia a ser filtrada: ');
faixa_ruido = np.arange(inicio, fim+1)#dado em Hertz
faixa_transicao = 200; #do filtro e dado em Hertz
atenuacao_filtro = 20; #dado em dB
wp1= min(faixa_ruido) - faixa_transicao;
ws1= min(faixa_ruido);
ws2= max(faixa_ruido);
wp2= max(faixa_ruido) + faixa_transicao;
#normaliza em funcao da freq Nysquest = Fs/2.
wp1= wp1/(Fs/2);
ws1= ws1/(Fs/2);
ws2= ws2/(Fs/2);
wp2= wp2/(Fs/2);
[n, wn]=sigs.buttord(concatenate((wp1, wp2)), concatenate((ws1, ws2)), 1, atenuacao_filtro);
[b, a]= sigs.butter(n,wn,'stop'); #calcula coeficientes filtro rejeita-banda
musica_filtrada = filter(b,a,musica_original);

## Parte 6: calcula espectro musica filtrada
espectro_musica_filtrada = abs(fft(musica_filtrada));
N = len(musica_filtrada);
m = np.arange(0, N)
freq_espectro_filtrado = m*Fs/N;
espectro_musica_filtrada = espectro_musica_filtrada[0:round(N/2)];
freq_espectro_filtrado = freq_espectro_filtrado[0:round(N/2)];
plt.subplot(4,1,3); plt.plot(musica_filtrada); plt.title('Música filtrada');
plt.subplot(4,1,4); plt.plot(freq_espectro_filtrado,espectro_musica_filtrada); plt.title('Espectro sinal filtrado');


#audiowrite('ATOA_musica_filtrada_teste6.wav',musica_filtrada,Fs);
#scipy.io.wavfile.write(filename, rate, data)


write("ATOA_musica_filtrada_teste6.wav", Fs, musica_filtrada)