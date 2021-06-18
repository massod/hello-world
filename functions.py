def sigma(n):
	if n < 2:
		return n
	else:
		return n + sigma(n-1)


print(sigma(50))

