    clear; clc; close all;
%% Parte 1: gera ruido e plota seu espectro    
    dados = importdata('ATOA_musica_ruidosa_teste5.wav');
    musica_original = dados.data;
    Fs = dados.fs;
    espectro_original = abs(fft(musica_original));
    N = length(musica_original);
    m = 0:N-1;
    freq_espectro_original = m.*Fs/N;
    espectro_original = espectro_original(1:round(N/2));
    freq_espectro_original = freq_espectro_original(1:round(N/2));       
    subplot(4,1,1); plot(musica_original); title('musica original no tempo');
    subplot(4,1,2); plot(freq_espectro_original, espectro_original); title('Espectro sinal original'); 
    
%% Parte 1: projeta filtro para tirar ruido    
    inicio = input('Digite a primeira frequencia a ser filtrada: ');
    fim = input('Digite a ultima frequencia a ser filtrada: ');
    faixa_ruido = inicio:fim; %dado em Hertz
    faixa_transicao = 200; %do filtro e dado em Hertz
    atenuacao_filtro = 20; %dado em dB
    wp1= min(faixa_ruido) - faixa_transicao;
    ws1= min(faixa_ruido);
    ws2= max(faixa_ruido);
    wp2= max(faixa_ruido) + faixa_transicao;
    %normaliza em funcao da freq Nysquest = Fs/2.    
    wp1= wp1/(Fs/2);
    ws1= ws1/(Fs/2);
    ws2= ws2/(Fs/2);
    wp2= wp2/(Fs/2);    
    [n, wn]=buttord([wp1 wp2], [ws1 ws2], 1, atenuacao_filtro);
    [b, a]= butter(n,wn,'stop'); %calcula coeficientes filtro rejeita-banda
    musica_filtrada = filter(b,a,musica_original);    
    
%% Parte 6: calcula espectro musica filtrada
    espectro_musica_filtrada = abs(fft(musica_filtrada));
    N = length(musica_filtrada);
    m = 0:N-1;
    freq_espectro_filtrado = m.*Fs/N;
    espectro_musica_filtrada = espectro_musica_filtrada(1:round(N/2));
    freq_espectro_filtrado = freq_espectro_filtrado(1:round(N/2));
    subplot(4,1,3); plot(musica_filtrada); title('Música filtrada');
    subplot(4,1,4); plot(freq_espectro_filtrado,espectro_musica_filtrada); title('Espectro sinal filtrado');
    audiowrite('ATOA_musica_filtrada_teste6.wav',musica_filtrada,Fs);