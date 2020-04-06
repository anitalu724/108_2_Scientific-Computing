% Main program for testing addAndMax.m

testCaseCount=10;

for i=1:testCaseCount
	m1=round(10+10*rand);
	n1=round(10+20*rand);
	m2=round(10+30*rand);
	n2=round(10+40*rand);
	a=rand(m1, n1);
	b=rand(m2, n2);
	out1=addAndMax(a, b);
	out2=addAndMaxSP(a, b);
	fprintf('Case=%d/%d, diff=%g\n', i, testCaseCount, abs(out1-out2));
end