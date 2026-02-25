class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for  i,j in enumerate(nums):
            diff=target-j
            if diff in d:
                return [d[diff]+1,i+1]
            d[j]=i
        return [-1,-1]
    
s=Solution()
print(s.twoSum([2,7,11,15],9))

# Time Complexity: O(n)
# Space Complexity: O(n)