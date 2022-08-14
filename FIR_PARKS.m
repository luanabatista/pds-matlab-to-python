%Ilustração do uso da função firpm que executa o algoritmo de Parks-McClellan para encontrar coeficientes de filtro FIR.
%coeficientes para filtro passa-faixa:
% f = [0 0.4 0.44 0.56 0.6 1];
% a = [0 0 1 1 0 0];
%coeficientes para filtro passa-baixas:
f = [0 0.4 0.5 1];
m = [1 1 0 0];
coef = firpm(32,f,m);
freqz(coef);