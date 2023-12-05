def check(arr, x):
    count = 0
    for i in range(0, len(arr)):
        if (arr[i] == x):
            count += 1

    if (count > 1):
        return False
    
    return True

nums = [1,2,3,4,5,5]
if(check(nums, 4) == True):
    print("Unique")
else:
    print("Not unique")