def second_largest_from_last(nums):
    if len(nums) < 2:
        return None

    max1 = max2 = float('-inf')
    
    for i in nums:
        if i>max1:
            max2 = max1
            max1 = i
        elif max1 > i > max2:
            max2 = i
    return max2 if max2 != float('-inf') else None

# Example usage:
nums = [3, 1, 4, 1, 5, 9]
result = second_largest_from_last(nums)
print(result)