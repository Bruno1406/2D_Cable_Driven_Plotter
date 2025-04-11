coord2len = @(x,y,L) [sqrt(x.^2 + y.^2), sqrt((L - x).^2 + y.^2)];

coord2len_dot = @(x, y, dx, dy,L) [ ...
    (x .* dx + y .* dy) ./ sqrt(x.^2 + y.^2), ...
    (-(L - x) .* dx + y .* dy) ./ sqrt((L - x).^2 + y.^2)];

coord2len_2dot = @(x, y, dx, dy, d2x, d2y,L) [ ...
    ((dx.^2 + x .* d2x + dy.^2 + y .* d2y) ./ sqrt(x.^2 + y.^2)), ...
    (((dx.^2 - (L - x) .* d2x + dy.^2 + y .* d2y)) ./ sqrt((L - x).^2 + y.^2)) ...
];

L = 0.3;
T = 6;
steps = 111;
dt = T/steps;

t = linspace(0, T, steps)';

%Circulo
x_ref = 0.08 * cos(2*pi*t/T) + 0.15;
y_ref = 0.08 * sin(2*pi*t/T) + 0.2;

%Triangulo
%l = 0.15;
%h = sqrt(3)/2 * l;

% Vértices (posição relativa ao centro)
%v1 = [0, 2/3*h];
%v2 = [-l/2, -1/3*h];
v3 = [ l/2, -1/3*h];

% Centro
cx = 0.15;
cy = 0.2;

% Vértices absolutos
p1 = [cx + v1(1), cy + v1(2)];
p2 = [cx + v2(1), cy + v2(2)];
p3 = [cx + v3(1), cy + v3(2)];

% Número de pontos por lado
n = steps / 3;

% Interpolação linear entre os vértices

dx_ref = num_derivative(x_ref,dt);
dy_ref = num_derivative(y_ref,dt);

d2x_ref = num_derivative(dx_ref,dt);
d2y_ref = num_derivative(dy_ref,dt);

q = coord2len(x_ref, y_ref,L);            
q_dot = coord2len_dot(x_ref, y_ref, dx_ref, dy_ref,L);
q_2dot = coord2len_2dot(x_ref, y_ref, dx_ref, dy_ref, d2x_ref, d2y_ref,L);
theta = calcula_pos(q, L);
theta_dot = calcula_vel(q,q_dot,theta);
theta_2dot = calcula_acel(q,q_dot,q_2dot,theta,theta_dot);

x_res = q(:,1).*cos(theta(:,1)); 
y_res = -q(:,1).*sin(theta(:,1)); 
dx_res = q_dot(:,1).*cos(theta(:,1)) - q(:,1).*sin(theta(:,1)).*theta_dot(:,1);
dy_res = -q_dot(:,1).*sin(theta(:,1)) - q(:,1).*cos(theta(:,1)).*theta_dot(:,1);
d2x_res = q_2dot(:,1).*cos(theta(:,1)) ...
        - 2*q_dot(:,1).*sin(theta(:,1)).*theta_dot(:,1) ...
        - q(:,1).*cos(theta(:,1)).*theta_dot(:,1).^2 ...
        - q(:,1).*sin(theta(:,1)).*theta_2dot(:,1);

d2y_res = -q_2dot(:,1).*sin(theta(:,1)) ...
        - 2*q_dot(:,1).*cos(theta(:,1)).*theta_dot(:,1) ...
        + q(:,1).*sin(theta(:,1)).*theta_dot(:,1).^2 ...
        - q(:,1).*cos(theta(:,1)).*theta_2dot(:,1);

figure;

subplot(2,1,1);
plot(x_res, y_res);
hold on;
xlabel('x');
ylabel('y');
title('Result Trajectory');
axis equal;
grid on;

subplot(2,1,2);
plot(x_ref, y_ref);
hold on;
xlabel('x');
ylabel('y');
title('Reference Trajectory');
axis equal;
grid on;

% Plot comparison of dx
figure;
subplot(2,1,1);
plot(t, dx_ref, 'b', 'DisplayName', 'dx_{ref} (m/s)');
hold on;
plot(t, dx_res, 'r--', 'DisplayName', 'dx_{res} (m/s)');
xlabel('Time [s]');
ylabel('dx [m/s]');
title('dx: Reference vs Result');
legend;
grid on;

subplot(2,1,2);
plot(t, dx_ref - dx_res, 'k');
xlabel('Time [s]');
ylabel('Error [m/s]');
title('dx Error (ref - res)');
grid on;

% Plot comparison of dy
figure;
subplot(2,1,1);
plot(t, dy_ref, 'b', 'DisplayName', 'dy_{ref} (m/s)');
hold on;
plot(t, dy_res, 'r--', 'DisplayName', 'dy_{res} (m/s)');
xlabel('Time [s]');
ylabel('dy [m/s]');
title('dy: Reference vs Result');
legend;
grid on;

subplot(2,1,2);
plot(t, dy_ref - dy_res, 'k');
xlabel('Time [s]');
ylabel('Error [m/s]');
title('dy Error (ref - res)');
grid on;

% Plot comparison of d2x
figure;
subplot(2,1,1);
plot(t, d2x_ref, 'b', 'DisplayName', 'd^2x_{ref} (m/s^2)');
hold on;
plot(t, d2x_res, 'r--', 'DisplayName', 'd^2x_{res} (m/s^2)');
xlabel('Time [s]');
ylabel('d^2x [m/s^2]');
title('d^2x: Reference vs Result');
legend;
grid on;

subplot(2,1,2);
plot(t, d2x_ref - d2x_res, 'k');
xlabel('Time [s]');
ylabel('Error [m/s^2]');
title('d^2x Error (ref - res)');
grid on;

% Plot comparison of d2y
figure;
subplot(2,1,1);
plot(t, d2y_ref, 'b', 'DisplayName', 'd^2y_{ref} (m/s^2)');
hold on;
plot(t, d2y_res, 'r--', 'DisplayName', 'd^2y_{res} (m/s^2)');
xlabel('Time [s]');
ylabel('d^2y [m/s^2]');
title('d^2y: Reference vs Result');
legend;
grid on;

subplot(2,1,2);
plot(t, d2y_ref - d2y_res, 'k');
xlabel('Time [s]');
ylabel('Error [m/s^2]');
title('d^2y Error (ref - res)');
grid on;

% Plot of theta1
figure;
subplot(3,1,1);
plot(t,theta(:,1),'b', 'DisplayName','\theta_{1} (rad)');
hold on;
xlabel('Time [s]');
ylabel('\theta_1 [rad]');
title('Angle 1');
legend;
grid on

subplot(3,1,2);
plot(t,theta_dot(:,1),'b', 'DisplayName','\dtheta_{1} (rad/s)');
hold on;
xlabel('Time [s]');
ylabel('d\theta_1 [rad/s]');
title('Angular Velocity 1');
legend;
grid on

subplot(3,1,3);
plot(t,theta_2dot(:,1),'b', 'DisplayName','\d2theta_{1} (rad/s^2)');
hold on;
xlabel('Time [s]');
ylabel('d2\theta_1 [rad/s^2]');
title('Angular acceleration 1');
legend;
grid on

% Plot of theta2
figure;
subplot(3,1,1);
plot(t,theta(:,2),'b', 'DisplayName','\theta_{2} (rad)');
hold on;
xlabel('Time [s]');
ylabel('\theta_2 [rad]');
title('Angle 2');
legend;
grid on

subplot(3,1,2);
plot(t,theta_dot(:,2),'b', 'DisplayName','\dtheta_{2} (rad/s)');
hold on;
xlabel('Time [s]');
ylabel('d\theta_2 [rad/s]');
title('Angular Velocity 2');
legend;
grid on

subplot(3,1,3);
plot(t,theta_2dot(:,2),'b', 'DisplayName','\d2theta_{2} (rad/s^2)');
hold on;
xlabel('Time [s]');
ylabel('d2\theta_2 [rad/s^2]');
title('Angular acceleration 2');
legend;
grid on

% Plot of q1
figure;
subplot(3,1,1);
plot(t,q(:,1),'b', 'DisplayName','q_{1} (m)');
hold on;
xlabel('Time [s]');
ylabel('q_1 [m]');
title('Lenght 1');
legend;
grid on

subplot(3,1,2);
plot(t,q_dot(:,1),'b', 'DisplayName','dq_{1} (m/s)');
hold on;
xlabel('Time [s]');
ylabel('dq_1 [m/s]');
title('Velocity 1');
legend;
grid on

subplot(3,1,3);
plot(t,q_2dot(:,1),'b', 'DisplayName','d2q_{1} (m/s^2)');
hold on;
xlabel('Time [s]');
ylabel('d2q_1 [m/s^2]');
title('Acceleration 1');
legend;
grid on

% Plot of q2
figure;
subplot(3,1,1);
plot(t,q(:,2),'b', 'DisplayName','q_{2} (m)');
hold on;
xlabel('Time [s]');
ylabel('q_2 [m]');
title('Lenght 2');
legend;
grid on

subplot(3,1,2);
plot(t,q_dot(:,2),'b', 'DisplayName','dq_{2} (m/s)');
hold on;
xlabel('Time [s]');
ylabel('dq_2 [m/s]');
title('Velocity 2');
legend;
grid on

subplot(3,1,3);
plot(t,q_2dot(:,2),'b', 'DisplayName','d2q_{2} (m/s^2)');
hold on;
xlabel('Time [s]');
ylabel('d2q_2 [m/s^2]');
title('Acceleration 2');
legend;
grid on

