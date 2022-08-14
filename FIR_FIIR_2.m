%- Projeto de um filtro FIR passa-baixas, passa-latas e faixas
%% PARTE 1: dados do filtro
Fs = 20000; %taxa de amostragem
fc = 2000; %frequencia de corte do filtro
N = 64; %Quantidade total de coeficientes filtro
Num_Coef_Filtro = 64; %Qtos coeficientes vou usar do total
tipo_filtro = input('\nTipo filtro(1=passa-baixas; 2=passa-altas; 3=passa-faixa) =');
%% PARTE 2: gera o espectro ideal do filtro
H = zeros(1,N); %resposta em freq ideal do filtro
f_resol = Fs/N; %calcula resolução frequencia
m_corte = round(fc/f_resol)+1; %estima indice "m" de fc
H = [ones(1, m_corte + 1) zeros(1, (N/2-m_corte)) zeros(1, (N/2-m_corte)) ones(1, m_corte- 1)]; %gera espectro ideal do filtro

m = 0:N-1;
f = m.*f_resol; %define o eixo de frequencias do grafico 1
%% PARTE 3: gera todos coef. ideais do filtro
h_ideal = ifft(H);
if (tipo_filtro==2) %se passa-alta, multiplicar coef por [1,-1,1,-1,...]
n = 0:N-1;
deslocamento_f = cos(2*pi*n.*(Fs/2)/Fs);
h_ideal = h_ideal.*deslocamento_f;
end
if (tipo_filtro==3) %se passa-faixa, multiplicar coef por modulacao
n = 0:N-1;
fcc = input('\nDigite em Hz frequência central =');
deslocamento_f = cos(2*pi*fcc.*n/Fs);
h_ideal = h_ideal.*deslocamento_f;
end
%% PARTE 4: GERA SIMETRIA PAR NA FUNCAO SYNC DOS COEFICIENTES
h_ideal(N/2:N) = h_ideal(1:N/2+1);
for i=2:(N/2)
h_ideal(i-1)= h_ideal(N-i+1);
end
inicio = N/2 - Num_Coef_Filtro/2 + 1;
fim = N/2 + Num_Coef_Filtro/2;
h = real(h_ideal(inicio:fim)); %pega so parte dos coeficientes ideias do filtro
%% PARTE 5 (opcional): aplica janela
resposta = input('\nDeseja aplicar janela aos coef (1=sim; 2=nao)? = ');
if (resposta == 1)
jan = window(@blackman,(fim-inicio)+1);
h = h.*jan';
end
%% PARTE 6: testa a implementação filtro com sinal sintetico
N_sinal_sintetico = 400; % quantidade de amostras do sinal sintetico
n1 = 0:N_sinal_sintetico-1;
entrada_discretizada = sin(2*pi*500.*n1/Fs) + sin(2*pi*2500.*n1/Fs) + sin(2*pi*5000.*n1/Fs)...
+ sin(2*pi*8000.*n1/Fs);
saida = conv(entrada_discretizada, h);
N_sinal_saida = size(saida,2);
N_resp_impulsitva = Num_Coef_Filtro;
%% PARTE 7: calcula espectros sinal entrada, saida e h(n)
fft_sinal_entrada = fft(entrada_discretizada)/N_sinal_sintetico;
fft_sinal_saida = fft(saida)/N_sinal_saida;
fft_resp_filtro = fft(h);
f_entrada = n1.*(Fs/N_sinal_sintetico);
n3 = 0:size(fft_sinal_saida,2)-1;
f_saida = n3.*(Fs/N_sinal_saida);
n2 = 0:size(fft_resp_filtro,2)-1;
f_h = n2.*(Fs/N_resp_impulsitva);
%% PARTE 8: plota
subplot(2,2,1); stem(f,H); title('H(f) idealizado'); xlabel('f(Hz)')
subplot(2,2,2); stem(real(h_ideal)); xlabel('n'); hold on; stem([inicio:fim],h,'-.r');
title('Coeficientes h(n) do filtro'); ylabel('Amplitude'); xlabel('n');
legend('Todos','Selecionados');
subplot(2,2,3); plot(f_entrada(1:N_sinal_sintetico/2),abs(fft_sinal_entrada(1:N_sinal_sintetico/2)));

hold on;
plot(f_saida(1:N_sinal_saida/2),abs(fft_sinal_saida(1:N_sinal_saida/2)),'r');

plot(f_h(1:N_resp_impulsitva/2),abs(fft_resp_filtro(1:N_resp_impulsitva/2)),'g');

legend('entrada','saída','resp. impulsiva');
xlabel('Freq (Hz)');
title('Espectros dos sinais e filtro')
subplot(2,2,4); plot(n1, entrada_discretizada);
hold on;
plot(n3, saida,'r');
legend('entrada','saída');
xlabel('n');
title('Sinais discretos do filtro');
% [mag,f] = freqz(h);
% plot(f/pi,abs(mag))
