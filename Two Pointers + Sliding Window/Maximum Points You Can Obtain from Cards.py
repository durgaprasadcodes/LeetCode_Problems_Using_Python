class Solution:
    def maxScore(self, nums,k) -> int:
        
        n=len(nums)
        if k>n:
            return 0
        if k==n:
            return sum(nums)

        max_sum=curr_sum=sum(nums[:k])
        l=k-1
        for r in range(n-1,n-k-1,-1):
            curr_sum+=(-nums[l]+nums[r])
            max_sum=max(max_sum,curr_sum)
            l-=1
        return max_sum
    
s=Solution()
print(s.maxScore([1,2,3,4,5,6,1],3))
print(s.maxScore([1,79,80,1,1,1,200,1],3))

# Time Complexity: O(k)
# Space Complexity: O(1)