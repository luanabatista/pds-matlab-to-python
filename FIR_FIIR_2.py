#Projeto de um filtro FIR passa-baixas, passa-altas e faixas
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft

def ctranspose(arr: np.ndarray) -> np.ndarray:
    tmp = arr.transpose()
    return tmp - 2j*tmp.imag

## PARTE 1: dados do filtro
Fs = 20000; # taxa de amostragem
fc = 2000; # frequencia de corte do filtro
N = 64; # Quantidade total de coeficientes filtro
Num_Coef_Filtro = 64; # Qtos coeficientes vou usar do total
tipo_filtro = input('\nTipo filtro(1=passa-baixas; 2=passa-altas; 3=passa-faixa) = ');

## PARTE 2: gera o espectro ideal do filtro
aux = np.zeros((1,N))
H = aux[0]; # resposta em freq ideal do filtro
f_resol = Fs/N; # calcula resolução frequencia
m_corte = round(fc/f_resol)+1; # estima indice "m" de fc

H = np.concatenate((np.ones((1, m_corte + 1))[0], np.zeros((1, int(N/2-m_corte)))[0], np.zeros((1, int(N/2-m_corte)))[0], np.ones((1, m_corte- 1))[0])); # gera espectro ideal do filtro
m = np.arange(0, N)
f = m*f_resol; # define o eixo de frequencias do grafico 1

## PARTE 3: gera todos coef. ideais do filtro
h_ideal = fft.ifft(H);
if (tipo_filtro==2): # se passa-alta, multiplicar coef por [1,-1,1,-1,...]
    n = np.arange(0, N)
    deslocamento_f = np.cos(2*np.pi*n*(Fs/2)/Fs);
    h_ideal = h_ideal*deslocamento_f;

if (tipo_filtro==3): # se passa-faixa, multiplicar coef por modulacao
    n = np.arange(0, N)
    fcc = input('\nDigite em Hz frequência central =');
    deslocamento_f = np.cos(2*np.pi*fcc*n/Fs);
    h_ideal = h_ideal*deslocamento_f;

## PARTE 4: GERA SIMETRIA PAR NA FUNCAO SYNC DOS COEFICIENTES
h_ideal[int((N/2)-1):N] = h_ideal[0:int((N/2)+1)]; 
for i in range(2,int(N/2+1)):
    h_ideal[i-1]= h_ideal[N-i+1]

inicio = int(N/2 - Num_Coef_Filtro/2 + 1);
fim = int(N/2 + Num_Coef_Filtro/2)

h = (h_ideal[inicio-1:fim]).real; # pega so parte dos coeficientes ideias do filtro

## PARTE 5 (opcional): aplica janela
resposta = input('\nDeseja aplicar janela aos coef (1=sim; 2=nao)? = ')
if (resposta == 1):
    #jan = window(@blackman,(fim-inicio)+1)
    jan = np.blackman((fim-inicio)+1)
    h = ctranspose(h*jan)

## PARTE 6: testa a implementação filtro com sinal sintetico
N_sinal_sintetico = 400; # quantidade de amostras do sinal sintetico
n1 = np.arange(0, N_sinal_sintetico)
entrada_discretizada = np.sin(2*np.pi*500.*n1/Fs) + np.sin(2*np.pi*2500.*n1/Fs) + np.sin(2*np.pi*5000.*n1/Fs) + np.sin(2*np.pi*8000.*n1/Fs);
saida = np.convolve(entrada_discretizada, h);

N_sinal_saida = np.size(saida); #N_sinal_saida = size(saida,2);
N_resp_impulsitva = Num_Coef_Filtro;

## PARTE 7: calcula espectros sinal entrada, saida e h(n)
fft_sinal_entrada = fft.fft(entrada_discretizada)/N_sinal_sintetico;
fft_sinal_saida = fft.fft(saida)/N_sinal_saida;
fft_resp_filtro = fft.fft(h);
f_entrada = n1*(Fs/N_sinal_sintetico);
n3 = np.arange(0, np.size(fft_sinal_saida))
f_saida = n3*(Fs/N_sinal_saida);
n2 = np.arange(0, np.size(fft_resp_filtro))
f_h = n2*(Fs/N_resp_impulsitva);

## PARTE 8: plota
plt.subplot(2,2,1); plt.stem(f,H); plt.title('H(f) idealizado'); plt.xlabel('f(Hz)')
plt.subplot(2,2,2); plt.stem((h_ideal).real); plt.xlabel('n'); 
plt.title('Coeficientes h(n) do filtro'); plt.ylabel('Amplitude'); plt.xlabel('n');

plt.subplot(2,2,3); plt.plot(f_entrada[0:int(N_sinal_sintetico/2)],abs(fft_sinal_entrada[0:int(N_sinal_sintetico/2)]), label='entrada');
plt.plot(f_saida[0:int(N_sinal_saida/2)],abs(fft_sinal_saida[0:int(N_sinal_saida/2)]),'r', label='saída');
plt.plot(f_h[0:int(N_resp_impulsitva/2)],abs(fft_resp_filtro[0:int(N_resp_impulsitva/2)]),'g', label='resp. impulsiva');
plt.legend();

plt.xlabel('Freq (Hz)');
plt.title('Espectros dos sinais e filtro')
plt.subplot(2,2,4); plt.plot(n1, entrada_discretizada, label='entrada');
plt.plot(n3, saida,'r', label='saída');
plt.legend();
plt.xlabel('n');
plt.title('Sinais discretos do filtro');
plt.show()