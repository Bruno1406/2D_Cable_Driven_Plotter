function [theta_2dot] = calcula_acel(q,q_dot,q_2dot, theta, theta_dot)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
n = length(q);
theta_2dot = zeros(n,2);
for i = 1:n
     A = [-q(i,1)*sin(theta(i,1)), -q(i,2)*sin(theta(i,2)); ...
         q(i,1)*cos(theta(i,1)), q(i,2)*cos(theta(i,2))];
     B = [-q_2dot(i,1)*cos(theta(i,1)) + 2*q_dot(i,1)*sin(theta(i,1))*theta_dot(i,1) + q(i,1)*theta_dot(i,1)^2*cos(theta(i,1))+  ...
          -q_2dot(i,2)*cos(theta(i,2)) + 2*q_dot(i,2)*sin(theta(i,2))*theta_dot(i,2) + q(i,2)*theta_dot(i,2)^2*cos(theta(i,2)); ...
          -q_2dot(i,1)*sin(theta(i,1)) - 2*q_dot(i,1)*cos(theta(i,1))*theta_dot(i,1) + q(i,1)*theta_dot(i,1)^2*sin(theta(i,1))+  ...
          -q_2dot(i,2)*sin(theta(i,2)) - 2*q_dot(i,2)*cos(theta(i,2))*theta_dot(i,2) + q(i,2)*theta_dot(i,2)^2*sin(theta(i,2))];
     theta_2dot(i,:) = linsolve(A,B)';
end
end