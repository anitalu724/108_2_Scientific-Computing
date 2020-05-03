function [theta, sse]=ellipseFit(data)
% Ellipse fitting

x = data(:, 1);
y = data(:, 2);
center_init = [mean(x), mean(y)]


[sse, radius] = sseOfEllipseFit(center_init, data);
[center, sse] = fminsearch(@(center) errorMeasure(center, data, radius), center_init);


theta = [center(1), center(2), radius(1), radius(2)];
...

% Function that returns SSE and the linear parameters
function [sse, radius]=sseOfEllipseFit(center, data)
[n, d] = size(data);
center_2 = [];
for i = 1:n
    center_2 = [center_2; center];
end
center_2
theta = (data - center_2) .^ 2 \ ones(n, 1);
radius = 1 ./ theta .^ 0.5;
sse = sum(((data - center_2) .^ 2 * theta - ones(n, 1)) .^ 2);
