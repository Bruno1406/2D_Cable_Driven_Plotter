% Define plotter parameters as Simulink.Parameter objects

K_t = 0.009;
L_a = 0.0023;
R_a = 2.182;
J_m = 0.000004;
B_m = 0.000002;
Gr  = 1/30;
L   = 0.3;
K   = 2040;
C   = 15;
m   = 0.1;
g   = 9.8;
R   = 0.017;
alfa = cos(0.34906585);

set_points = readtable('setpoint.csv');
% Extract the columns into variables
t = set_points.t;
left_ticks = set_points.tick_left;
right_ticks = set_points.tick_right;

left_signal = [t,left_ticks];
right_signal = [t, right_ticks];