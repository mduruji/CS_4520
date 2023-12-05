def binaryNumsCount(x):
    count = 1
    while x > 1:
        count += 1
        x /= 2

    return count

print(binaryNumsCount(50))