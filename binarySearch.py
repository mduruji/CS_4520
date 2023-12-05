def search(nums, target):
   f = 0
   l = len(nums)-1

   mid = f + ((f+l)//2)

   if(nums[mid] == target):
      return True
   elif(nums[mid] < target):
      return search(nums[mid + 1: ], target)
   else:
      return search(nums[: mid -1], target)
   
a = [1,2,4,5,6]
targ = 6

if(search(a, targ) == True):
   print(a.index(targ))
