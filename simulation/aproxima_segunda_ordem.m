% Dados experimentais
dados = [
    0.000000, 0; 0.025600, 45; 0.051201, 53; 0.076800, 99; 0.102400, 141;
    0.127998, 142; 0.153600, 180; 0.179200, 186; 0.204800, 196; 0.230400, 219;
    0.255996, 215; 0.281600, 227; 0.307200, 237; 0.332800, 236; 0.358400, 242;
    0.384000, 251; 0.409600, 249; 0.435192, 257; 0.460800, 261; 0.486400, 259;
    0.511992, 262; 0.537600, 267; 0.563200, 266; 0.588800, 268; 0.614400, 271;
    0.640000, 272; 0.665600, 272; 0.691200, 275; 0.716800, 275; 0.742400, 274;
    0.768000, 277; 0.793600, 280; 0.819200, 277; 0.844800, 277; 0.870384, 282;
    0.896000, 282; 0.921600, 280; 0.947200, 280; 0.972800, 283; 0.998400, 283
];
tempo = dados(:, 1);
velocidade = dados(:, 2) * (2 *pi /(12* 1920));

% Função de resposta ao degrau de sistema de 2ª ordem subamortecido
resposta_segunda_ordem = @(p, t) p(1) * (1 - (1 ./ sqrt(1 - p(2)^2)) .* ...
    exp(-p(2) * p(3) * t) .* sin(p(3) * sqrt(1 - p(2)^2) * t + acos(p(2))));

% Chutes iniciais: [K, zeta, wn]
p0 = [max(velocidade), 0.5, 10];

% Ajuste com lsqcurvefit
options = optimset('Display','off');
p_otimos = lsqcurvefit(resposta_segunda_ordem, p0, tempo, velocidade, [], [], options);

% Parâmetros ajustados
K = p_otimos(1);
zeta = p_otimos(2);
wn = p_otimos(3);

% Geração da curva ajustada
tempo_fit = linspace(min(tempo), max(tempo), 500);
velocidade_fit = resposta_segunda_ordem(p_otimos, tempo_fit);

% Plot
figure;
plot(tempo, velocidade, 'bo', 'DisplayName', 'Dados experimentais');
hold on;
plot(tempo_fit, velocidade_fit, 'r-', 'LineWidth', 2, 'DisplayName', ...
    sprintf('Modelo 2ª ordem ajustado\nK=%.2f, ζ=%.2f, ω_n=%.2f', K, zeta, wn));
xlabel('Tempo (s)');
ylabel('Velocidade');
title('Ajuste de Sistema de Segunda Ordem');
legend('Location', 'southeast');
grid on;
