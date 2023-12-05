def gcd(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    
    return m

print(gcd(60, 12))