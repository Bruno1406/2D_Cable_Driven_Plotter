function [f_dot] = num_derivative(f,dt)

% Numerical derivatives using central differences
f_dot = zeros(size(f));

% Central difference for interior points
f_dot(2:end-1) = (f(3:end) - f(1:end-2)) / (2*dt);

% Forward/backward difference for endpoints
f_dot(1) = (f(2) - f(1)) / dt;
f_dot(end) = (f(end) - f(end-1)) / dt;
end