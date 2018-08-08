def sum(n):
    primes = [2]
    runningtotal = 2
    test = 3
    while test < n:
        if all(test % prime != 0 for prime in primes):
            primes.append(test)
            runningtotal += test
        test += 2
    return runningtotal

print(sum(2000000))
