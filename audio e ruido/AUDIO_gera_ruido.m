    clear; clc; close all;
    dados = importdata('Cap1_Teste_5_musica.mp3');    
    
%% Parte 1: pega a musica, soma canais L+R e segmenta um pedaco    
    musica = dados.data;
    Fs = dados.fs;
    musica = musica(:,1) + musica(:,2); %somando canal esquerdo e direito
    subplot(3,2,1); plot(musica); title('musica no dominio n');
    inicio = input('Digite o INICIO n do trecho da musica (0=default) : ');
    if(inicio == 0)
        inicio = 11.9e+6; %a musica do LedZepplin tem um comeco legal aqui
    end
    fim = input('Digite o FIM n do trecho da musica (0=default) : ');
    if(fim == 0)
        fim = 1.474e+7; %a musica do LedZepplin tem um comeco legal aqui
    end
    segmento_musica_original = musica(inicio:fim,1); %segmentado
    hold on;
    plot(inicio:fim, segmento_musica_original, 'r');
        
%% Parte 2: exibe espectro do segmento da musica original
    espectro_original = abs(fft(segmento_musica_original));
    N = length(segmento_musica_original);
    m = 0:N-1;
    freq_espectro_original = m.*Fs/N;
    espectro_original = espectro_original(1:round(N/2));
    freq_espectro_original = freq_espectro_original(1:round(N/2));
    subplot(3,2,2); plot(freq_espectro_original,espectro_original); title('Espectro sinal original segmentado');    
     
%% Parte 3: gera ruido e plota seu espectro    
    freq_ini_ruido = input('Digite a primeira frequencia do ruido (0=sem ruido) : ');
    freq_fim_ruido = input('Digite a ultima frequencia do ruido (0=sem ruido) : ');
    amplitude      = input('Digite a AMPLITUDE do ruido (0=default) que pode ser no máximo 0.2: ');
    if((amplitude == 0) || amplitude > 0.2)
        amplitude = 0.01;
    end
    ruido = zeros(N,1);
    n=0:N-1;
    if((freq_ini_ruido ~= 0) )
        faixa_ruido = freq_ini_ruido:freq_fim_ruido;
        for i=1:length(faixa_ruido)
            freq_analo = faixa_ruido(i);
            temp = amplitude*sin(2*pi*freq_analo*n/Fs);
            ruido = ruido + temp';
        end
    end
    espectro_ruido = abs(fft(ruido));
    espectro_ruido = espectro_ruido(1:round(N/2));
    subplot(3,2,3); plot(ruido); title('Sinal de ruído no tempo');
    subplot(3,2,4); plot(freq_espectro_original,espectro_ruido); title('Espectro do ruído');
     
%% Parte 4: soma ruido e plota seu espectro
    musica_ruidosa = segmento_musica_original + ruido;
    audiowrite('ATOA_musica_ruidosa_teste5.wav', musica_ruidosa,Fs);
    fprintf('\nSalvou musica ruidosa com o nome ATOA_musica_ruidosa_teste5.wav\n');
    espectro_musica_ruido = abs(fft(musica_ruidosa));
    espectro_musica_ruido = espectro_musica_ruido(1:round(N/2));
    subplot(3,2,5); plot(musica_ruidosa); title('Musica com ruido no tempo');
    subplot(3,2,6); plot(freq_espectro_original,espectro_musica_ruido);    