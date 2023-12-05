def strMatch(biggerStr, smallerStr):
    if len(smallerStr) > len(biggerStr):
        return False

    for i in range(len(biggerStr) - len(smallerStr) + 1):
        if biggerStr[i:i + len(smallerStr)] == smallerStr:
            return True

    return False

a = "NOBODY_NOTICED_HIM"
b = "NOTICED"

print(strMatch(a, b))