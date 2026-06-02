class Solution(object):
    def sortedSquares(self, nums):
        if not nums:
            return []
        i=0
        j=len(nums)-1
        res=[]
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                res.append(nums[i]**2)
                i+=1
            else:
                res.append(nums[j]**2)
                j-=1
        return res[::-1]

s=Solution()
print(s.sortedSquares( [-7,-3,2,3,11]))

# Time Complexity: O(n)
# Space Complexity: O(n)
