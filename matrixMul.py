def mul(arr1, arr2):
    n = len(arr1)
    arr3 = [[0 for _ in range(n)] for _ in range(n)]

    if (len(arr1) != len(arr2)):
        return None
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                arr3[i][j] += arr1[i][k] * arr2[k][j]

    print(arr3)

arr1 = [[2,4], [3,5]]
arr2 = [[7,10], [6,9]]

mul(arr1, arr2)