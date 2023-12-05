def insertionSort(arr):
    for i in range(len(arr)):
        v = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > v:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = v
    return arr

x = [6,5,4,3,2,1]
print(insertionSort(x))