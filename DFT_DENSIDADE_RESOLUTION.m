%diferença entre resolução espectral e densidade espectral

clc; clear;
n = [0:99];
Fs = 100;
x = cos(0.48*pi*n) + cos(0.52*pi*n);
%% calcula DFT com N=10 e plota
n1 = [0:9];
sinal1 = x(1:10);
Y1 = dft(sinal1, 10);
magY1 = abs(Y1(1:6));
N1 = 5;
m1= 0:5;
f1= m1*Fs/N1;
subplot(2,3,1); stem(sinal1); xlabel('n'); title('N=10')
subplot(2,3,4); stem(f1, magY1); xlabel('freq(Hz)');
%% calc DFT com N=10+90 zeros e plota (melhor resol espectro)
sinal2 = [x(1:10) zeros(1,90)]; %preencheu sinal que essencialmente eh o mesmo
Y2 = dft(sinal2,100);
magY2 = abs(Y2(1:50));
N2 = 50;
m2= 1:50;
f2= m2*Fs/N2;
subplot(2,3,2); stem(sinal2); xlabel('n'); title('N=10+90 zeros com boa resol. espec.')
subplot(2,3,5); stem(f2, magY2); xlabel('freq(Hz)');
%% calc DFT com N=100
sinal3 = x(1:100);
Y3 = dft(sinal3,100);
magY3 = abs(Y3(1:50));
N3 = 50;
m3= 1:50;
f3= m3*Fs/N3;
subplot(2,3,3); stem(sinal3); xlabel('n'); title('N=100 com boa densid. espec.')
subplot(2,3,6); stem(f3, magY3); xlabel('freq(Hz)');