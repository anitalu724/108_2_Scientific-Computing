function output = addAndMax(A,B)
[m1 n1] = size(A);
[m2 n2] = size(B);
if m1 < m2
    m = m2;
else
    m = m1;
end
if n1 < n2
    n = n2;
else
    n = n1;
end
C = zeros(m,n);

for i = 1:m
    for j = 1:n
        if i <= m1 & i <= m2 & j <= n1 & j <= n2
            C(i,j) = A(i,j) + B(i,j);
        elseif i > m1 & j <= n2
            C(i,j) = B(i,j);
        elseif j > n2 & i <= m1
            C(i,j) = A(i,j);
        else
            C(i,j) = 0;
        end
    end
end

max = C(1);
for i = 1:m*n
    if max < C(i)
        max = C(i);
    end
end
output = max;