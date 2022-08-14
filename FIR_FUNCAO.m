%FILTRO USANDO FUNÇÃO FIR1 - Cálculos coeficientes filtro FIR usando função FIR1
ordem = 50;
resol_plot_freq = 512;
%Exemplo 1a: passa-baixas (frequência normalizada)
coef = fir1(ordem, 0.3);
freqz(coef,1,resol_plot_freq)
%Exemplo 1b: passa-baixas (frequência nominal considerando Fs=20k)
fc = 3000;
Fs = 20e3;
coef = fir1(ordem, fc/(Fs/2));
[H , freq] = freqz(coef,1,resol_plot_freq, 20e3);
plot(freq,abs(H));
% %Exemplo 2: passa-altas
% coef = fir1(ordem, 0.4,'high');
% freqz(coef,1,resol_plot_freq)
% %Exemplo 3: passa-altas com janela de Hanning
% coef = fir1(ordem, 0.6, 'high', hann(ordem+1));
% freqz(coef,1,resol_plot_freq)
% %Exemplo 4: passabanda
% coef = fir1(ordem, [0.3 0.5]);
% freqz(coef,1,resol_plot_freq)
% %Exemplo 5: rejeita-banda
% coef = fir1(ordem, [0.3 0.7], 'stop');
% freqz(coef,1,resol_plot_freq)