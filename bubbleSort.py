def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                swap(arr, i, j)
    return arr

x = [6,5,4,3,2,1]
print(bubSort(x))