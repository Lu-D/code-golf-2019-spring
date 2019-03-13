def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True
a = 3
b = 5
c = False
for i in range (2, 100000):
	if b - a == 2 and not c:
		print(a, " ", b, "\n")
		c = True
	if is_prime(i):
		a = b
		b = i
		c = False