def quick_sort(nums):
    if len(nums)<=1:
        return nums
    pivot  = nums[len(nums)//2]
    
    left =   [x for x in nums if x < pivot ]
    middle = [x for x in nums if x == pivot]
    right =  [x for x in nums if x > pivot ]
    
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([3,4,5,6,2,1,8,9,0]))