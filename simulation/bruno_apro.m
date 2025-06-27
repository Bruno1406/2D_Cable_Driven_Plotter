% Dados fornecidos
K_form1 = 23.26;
zeta_form1 = 5.39;
wn_form1 = 64.34;

Ra = 13.4;
J = 0.002143;

% Termos da primeira forma da função de transferência
numerator_form1 = K_form1 * wn_form1^2;
s_coeff_form1 = 2 * zeta_form1 * wn_form1;
constant_term_form1 = wn_form1^2;

% Definir as variáveis simbólicas
syms La Kt b

% Equações baseadas na comparação dos coeficientes

% Equação 1: Comparando os termos constantes do denominador
% wn_form1^2 = (Ra * b + Kt^2) / (J * La)
eq1 = constant_term_form1 == (Ra * b + Kt^2) / (J * La);

% Equação 2: Comparando os coeficientes de s do denominador
% 2 * zeta_form1 * wn_form1 = b/J + Ra/La
eq2 = s_coeff_form1 == b/J + Ra/La;

% Equação 3: Comparando os numeradores
% K_form1 * wn_form1^2 = Kt / (J * La)
eq3 = numerator_form1 == Kt / (J * La);

% Resolver o sistema de equações
[solLa, solKt, solb] = solve([eq1, eq2, eq3], [La, Kt, b]);

% Exibir os resultados
disp('Valores das variáveis encontradas:');
disp(['La = ', num2str(double(solLa)), ' H']);
disp(['Kt = ', num2str(double(solKt)), ' N.m/A (ou V.s/rad)']);
disp(['b = ', num2str(double(solb)), ' N.m.s/rad']);

% Opcional: Verificar se os valores encontrados fazem sentido
% Substituir os valores na segunda forma da FT para verificar
numerator_check = double(solKt) / (J * double(solLa));
s_coeff_check = double(solb) / J + Ra / double(solLa);
constant_term_check = (Ra * double(solb) + double(solKt)^2) / (J * double(solLa));

disp(' ');
disp('Verificação dos coeficientes da segunda forma da FT com os valores encontrados:');
disp(['Numerador verificado: ', num2str(numerator_check)]);
disp(['Coeficiente de s verificado: ', num2str(s_coeff_check)]);
disp(['Termo constante verificado: ', num2str(constant_term_check)]);

disp(' ');
disp('Valores esperados da primeira forma da FT:');
disp(['Numerador esperado: ', num2str(numerator_form1)]);
disp(['Coeficiente de s esperado: ', num2str(s_coeff_form1)]);
disp(['Termo constante esperado: ', num2str(constant_term_form1)]);