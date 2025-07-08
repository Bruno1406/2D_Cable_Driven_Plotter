
f = @(t,T,theta) 6*theta*(t/T)^5 - 15*theta*(t/T)^4 + 10*theta*(t/T)^3;
df = @(t,T,theta) 30*theta*t^4/T^5 - 60*theta*t^3/T^4 + 30*theta*t^2/T^3;
d2f = @(t,T,theta) 120*theta*t^3/T^5 - 180*theta*t^2/T^4 + 60*theta*t/T^3;

calculate_acceleration_norm = @(t,T,theta,R) R*sqrt(d2f(t,T,theta)^2 + df(t,T,theta)^4);


% Define the grid for the parameters
T_vec = linspace(0.1, 15, 100);     
Theta_vec = linspace(0.02, 2*pi, 100); 
R_vec = linspace(5, 150, 100);  

% Get grid sizes
num_T = length(T_vec);
num_Theta = length(Theta_vec);
num_R = length(R_vec);

% Pre-allocate a matrix to store the results
% Columns: T, Theta, R, A_max
results_data = zeros(num_T * num_Theta * num_R, 4);
counter = 1;

fprintf('Starting parameter space calculation...\n');

% Loop through the entire grid
for i = 1:num_T
    for j = 1:num_Theta
        for k = 1:num_R
            % Get current parameters
            T_current = T_vec(i);
            Theta_current = Theta_vec(j);
            R_current = R_vec(k);

            % Define the function to be minimized (negative of acceleration)
            % This is a function of 't' only, for the current parameters
            fun_to_minimize = @(t) -calculate_acceleration_norm(t, T_current, Theta_current, R_current);

            % Find the time 't' where the max acceleration occurs
            % and the value of that max acceleration
            % We search for t in the interval [0, T_current]
            [t_max_acc, neg_A_max] = fminbnd(fun_to_minimize, 0, T_current);

            % The maximum acceleration is the negative of the minimum found
            A_max = -neg_A_max;

            % Store the results
            results_data(counter, :) = [T_current, Theta_current, R_current, A_max];
            counter = counter + 1;
        end
    end
    fprintf('Completed T = %.2f (%d of %d)\n', T_vec(i), i, num_T);
end

fprintf('Calculation complete!\n');

logical_index = results_data(:, 4) >= 100 & results_data(:, 4) <= 2000;
results_data = results_data(logical_index, :); 
% Load or define your data (assuming results_data is already loaded)
T_data     = results_data(:, 1);
Theta_data = results_data(:, 2);
R_data     = results_data(:, 3);
A_max_data = results_data(:, 4);

% % Create second-order polynomial features
x_data = [Theta_data, R_data, A_max_data];  % Linear terms


fprintf('One parameter model\n');
fun = @(x, x_data) x(1) * sqrt( x_data(:,2) .* x_data(:,1) .* sqrt(1 + x_data(:,1).^2) ./ x_data(:,3) );

x0 = 1;

% Perform nonlinear least squares fitting
x_fit = lsqcurvefit(fun, x0, x_data, T_data, [], []);

% Display fitted coefficients
fprintf('Fitted coefficients:\n');
display(x_fit);

% Compute predictions and errors
T_predicted = fun(x_fit, x_data);
residuals = T_data - T_predicted;
mse = mean(residuals.^2);
max_abs_error = max(abs(residuals));

% Display errors
fprintf('\nMean Squared Error (MSE): %.4f\n', mse);
fprintf('Maximum Absolute Error: %.4f\n', max_abs_error);

% Plot actual vs predicted
figure;
scatter(T_data, T_predicted, 'b');
hold on;
plot([min(T_data), max(T_data)], [min(T_data), max(T_data)], 'r--');
xlabel('Actual T');
ylabel('Predicted T');
title('One Parameter Model: Actual vs Predicted');
grid on;

fprintf('Two parameters model\n');
fun = @(x, x_data) x(1) * (x_data(:,2) .* x_data(:,1) .* sqrt(1 + x_data(:,1).^2) ./ x_data(:,3)).^x(2);

x0 = [1,1];

% Perform nonlinear least squares fitting
x_fit = lsqcurvefit(fun, x0, x_data, T_data, [], []);

% Display fitted coefficients
fprintf('Fitted coefficients:\n');
display(x_fit);

% Compute predictions and errors
T_predicted = fun(x_fit, x_data);
residuals = T_data - T_predicted;
mse = mean(residuals.^2);
max_abs_error = max(abs(residuals));

% Display errors
fprintf('\nMean Squared Error (MSE): %.4f\n', mse);
fprintf('Maximum Absolute Error: %.4f\n', max_abs_error);

% Plot actual vs predicted
figure;
scatter(T_data, T_predicted, 'b');
hold on;
plot([min(T_data), max(T_data)], [min(T_data), max(T_data)], 'r--');
xlabel('Actual T');
ylabel('Predicted T');
title('Two parameter Model: Actual vs Predicted');
grid on;

