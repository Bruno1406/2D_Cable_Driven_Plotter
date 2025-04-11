function [theta_dot] = calcula_vel(q,q_dot,theta)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
n = length(q);
theta_dot = zeros(n,2);
for i = 1:n
    A = [-q(i,1)*sin(theta(i,1)), -q(i,2)*sin(theta(i,2)); ...
         q(i,1)*cos(theta(i,1)), q(i,2)*cos(theta(i,2))];
    B = [-q_dot(i,1)*cos(theta(i,1)) - q_dot(i,2)*cos(theta(i,2)); ...
         -q_dot(i,1)*sin(theta(i,1)) - q_dot(i,2)*sin(theta(i,2))];
    theta_dot(i,:) = linsolve(A,B)';
end
end