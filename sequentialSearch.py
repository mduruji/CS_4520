def find(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return "found at index " + i
    return "not found"

nums = [1,2,3,4,5,5]
print(find(nums, 7))