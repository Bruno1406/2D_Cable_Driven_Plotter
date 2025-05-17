function [theta] = calcula_pos(q, L)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
n = length(q);
theta = zeros(size(q));
x0 = [pi + pi/2, pi/3];
for i = 1:n
    f = @(x) [q(i,1)*cos(x(1)) + q(i,2)*cos(x(2)) - L ...
              q(i,1)*sin(x(1)) + q(i,2)*sin(x(2))];
    y = fsolve(f,x0);
    theta(i,:) = y;
    x0 = y;
end
end