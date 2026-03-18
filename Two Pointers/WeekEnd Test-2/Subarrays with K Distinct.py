class Solution:
    def minSubArrayLen(self, target ,nums):
        if len(nums)==1:
            return 1 if  nums[0]>=target else 0
        run_sum=0
        max_sum=float('inf')
        l=0
        for r in range(len(nums)):
            run_sum+=nums[r]
            while run_sum>=target:
                max_sum=min(max_sum,r-l+1)
                run_sum-=nums[l]
                if run_sum<0:
                    run_sum=0
                l+=1
        return max_sum if max_sum != float('inf') else 0

s=Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]))