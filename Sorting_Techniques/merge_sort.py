def merge_sort(nums:list):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    i = 0
    j = 0
    k = 0
    while i < len(left) and j <len(right):
        if left[i]<right[j]:
            nums[k] = left[i]
            i+=1
        else:
            nums[k] = right[j]
            j+=1
        k+=1
        
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
    return nums

# array = [4,3,5,2,2,5,6,7,8,3,2,1,0]
# print(merge_sort(array))
