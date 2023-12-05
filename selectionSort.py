def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selSort(arr):
    for i in range(0, len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
                swap(arr, i, min)
    return arr

x = [6,5,4,3,2,1]
print(selSort(x))