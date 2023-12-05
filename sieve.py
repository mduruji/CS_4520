def sieve(x):
    if x < 1: return None
    else: 
        primes = [True] * x

    primes[0] = primes[1] = False

    p = 2
    while p < x:
        for i in range(p*p, x, p):
            primes[i] = False
        p += 1

    primeNumbers = []
    for nums, isPrime in enumerate(primes):
        if isPrime:
            primeNumbers.append(nums)

    return primeNumbers
    
print(sieve(40))