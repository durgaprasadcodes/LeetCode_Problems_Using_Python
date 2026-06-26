def insertion_sort(nums):
    if len(nums)<=1:
        return nums
    for i in range(1,len(nums)):
        j = i-1
        temp = nums[i]
        while j>=0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = temp
    return nums
print(insertion_sort([4,3,5,3,7,2,8,1,9]))
print(insertion_sort([1,2,3,5,6,4]))