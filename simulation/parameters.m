% Define plotter parameters as Simulink.Parameter objects

K_t = 0.01;
L_a = 0.0048436939;
R_a = 2.2;
J_m = 0.000004;
B_m = 0.000001;
Gr  = 1/30;
L   = 0.3;
K   = 2040;
C   = 15;
m   = 0.1;
g   = 9.8;
R   = 0.017;
alfa = cos(0.34906585);
tick_p_meter = 17975.15;
compare_to_volt = 0.01171875;

set_points = readtable('set_points.csv');
% Extract the columns into variables
t = set_points.time;
left_ticks = set_points.left_ticks;
right_ticks = set_points.right_ticks;

left_signal = [t,left_ticks];
right_signal = [t, right_ticks];

plot(t,left_ticks)