def strMatch(biggerStr, smallerStr):
    match = False
    for i in range(len(biggerStr)):
        if biggerStr[i] == smallerStr[0]:
            match = True
            k = i
            for j in range(len(smallerStr)):
                if smallerStr[j] != biggerStr[k]:
                    match = False
                    break
                k += 1
    
    return match

a = "NOBODY_NOTICED_HIM"
b = "NOTICED"

print(strMatch(a, b))