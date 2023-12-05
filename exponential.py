def expo(a, n):
    if n == 0:
        return 1
    return a * expo(a, n-1)

b = expo(5,3)
print(b)