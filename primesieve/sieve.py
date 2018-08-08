
def sieve(n):
	primes = [2]
	test = 3
	while len(primes) < n:
		if all(test % prime != 0 for prime in primes):
			primes.append(test)
		test += 2
	return primes[-1]



print(sieve(10001))
