def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def part(arr):
    p = arr[0]
    l = 0
    s = l

    for i in range(l+1, len(arr)):
        if arr[i] <= p:
            s += 1
            swap(arr, s, i)
    swap(arr, l, s)

    return arr

x = [4, 1, 10, 8, 7, 12, 9, 2, 15]
print("pivot: " + str(x[0]), "\n", part(x))