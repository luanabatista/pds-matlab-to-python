%Importar o audio
[a, fs]= audioread('feminino.wav');% Se tivesse duas colunas podemos somar as duas e multipllicar 0.5

d=length(a)/fs;
b=length(a); %comprimento do audio

%Graficar o formato da onda
t=linspace(0,d,b);
figure
plot(t,a)
title('Formato de onda')
xlabel('tempo')
ylabel('amplitude')
grid on

%Função da frequência
fdt=fft(a);
fdtc=fftshift(fft(a));
freq=linspace(-fs/2,fs/2,length(fdt));
mag=abs(fdt);
magc=abs(fdtc);
fase=angle(fdt);
fasec=angle(fdtc);
figure
plot(freq,mag)
title('Magnitude fft');
xlabel('Hz');
ylabel('amplitude')
grid on;
figure
plot(freq,(magc/max(magc)));%normalizar
title('Magnitude fftshift');
xlabel('Hz');
ylabel('amplitude')
grid on;
figure
plot (freq,fasec)
title('fase');
xlabel('Hz');
ylabel('graus');
grid on;
%%

%filtro pasabajas

%Exemplo 1b: passa-baixas (frequência nominal considerando Fs=20k)
fc = 1000;
Fs1 = 8e3;
ordem=32;
resol_plot_freq = 1000;
coef = fir1(ordem, (fc/(Fs1/2)));
[H , freq1] = freqz(coef,1,resol_plot_freq, Fs1);
figure
plot(freq1,abs(H));
title('Magnitude filtro');
xlabel('Hz');
ylabel('graus');
%graficar filtro e o sinal de entrada

%filtra
coeficientes=H'


saida = filter(coeficientes,1,a);
sound(a)
pause (3)
%sound (saida)
%grafico frequencia filtrado

saidafft=fft(saida)
magfil=abs(saidafft)
sound (magfil)
figure
plot(freq,(magfil/max(magfil)));%normalizar
title('Magnitude sinal filtrado');
xlabel('Hz');
ylabel('amplitude')
grid on;



