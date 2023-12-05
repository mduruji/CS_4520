def hoaresPart(arr, low, high):
    i = low + 1
    j = high
    piv = arr[low]

    while (i <= j):
        while(arr[i] < piv):
            i += 1
        
        while(arr[j] > piv):
            j -= 1

        if(i <= j):
            arr[i] , arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quickSort(arr, low, high):
    if (low < high):
        piv = hoaresPart(arr, low, high)

        quickSort(arr, low, piv)
        quickSort(arr, piv +1, high)

arr = ['e', 'x', 'a', 'm', 'p', 'l', 'e']
low = 0
high = len(arr)-1
quickSort(arr, low, high)
print(arr)