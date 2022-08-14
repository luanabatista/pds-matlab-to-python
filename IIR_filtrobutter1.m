fs=8000;
    wp1= 500;
    ws1= 750;
    %normaliza em funcao da freq Nysquest = Fs/2.    
    wp1= wp1/(fs/2);
    ws1= ws1/(fs/2);
    atenuacao_filtro=20;
    [ord, wn]=buttord(wp1,ws1, 1, atenuacao_filtro);
    [num, dem]= butter(ord,wn,'low');
    [H , freq3] = freqz(num,dem,512, fs);
plot(freq3,abs(H))
title('Magnitude filtro');
xlabel('Hz');
ylabel('graus');%