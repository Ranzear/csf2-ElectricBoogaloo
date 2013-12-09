n = 4
series = 'fibonacci'

i = 0
result = 0

if (series == 'fibonacci'):
	fib=0
	l1=1
	l2=0
	for i in range(1, n):
		fib = l1+l2
		l2 = l1
		l1 = fib
	result = fib
elif(series == 'sum'):
	for i in range(1, n+1):
		result += 3 * i
else:
	result = 'Invalid string'
print result
