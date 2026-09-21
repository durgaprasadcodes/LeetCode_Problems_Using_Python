class Solution:
    def maxSatisfied(self, nums: list[int], grumpy: list[int], minutes: int) -> int:
        
        n = len(nums)
        ans = 0
        for i in range(n):
            if not grumpy[i]:
                ans += nums[i]
                nums[i] = 0
        cur_sum = max_sum = sum(nums[:minutes])
        l = 0
        for r in range(minutes,n):
            cur_sum += (-nums[l]+nums[r])
            max_sum = max(max_sum,cur_sum)
            l+=1
        return ans + max_sum