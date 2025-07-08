clc;
clear;

% Given constants
Wn = 64.36;
Zeta = 5.4;
K = 23.26;
J = 0.002143;
Ra = 2.2;
Kt = 0.01;

% System of equations
% x(1) = La
% x(2) = b

equations = @(x) [
    Kt - J * K * Wn^2 * x(1);                                  % Kt - J*K*Wn^2*La = 0
    x(2)/J + Ra/x(1) - 2 * Zeta * Wn;                         % b/J + Ra/La - 2*Zeta*Wn = 0
    (Ra * x(2) + Kt^2) / (J * x(1)) - Wn^2                   % (Ra*b + Kt^2)/(J*La) - Wn^2 = 0
];

% Initial guess based on your estimates [La, b]
x0 = [1e-5, 1.7e-6];

% Solve using fsolve
options = optimoptions('fsolve', 'Display', 'iter'); % Use 'off' to suppress output
solution = fsolve(equations, x0, options);

% Extract results
La = solution(1);
b = solution(2);

% Display results
fprintf('La = %.10f H\n', La);
fprintf('Kt = %.10f Nm/A (Known)\n', Kt);
fprintf('b  = %.10f Nms/rad\n', b);
