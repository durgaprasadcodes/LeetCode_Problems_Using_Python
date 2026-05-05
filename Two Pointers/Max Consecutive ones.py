class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_ones=0
        curr=0
        for r in nums:
            curr+=r
            if r==0:
                curr=0
            max_ones=max_ones if max_ones>curr else curr
        return max_ones
    
s=Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))

# Time complexity: O(n)
# Space complexity: O(1)