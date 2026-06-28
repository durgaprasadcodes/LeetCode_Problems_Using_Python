class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort()
        idx = -1
        sum = 0
        while k:
            sum+= nums[idx]*mul 
            k-=1
            mul = mul - 1 if mul > 1 else 1
            idx-=1
        return sum
            
            
s = Solution()
print(s.maxSum( [6,1,2,9], k = 3, mul = 2))