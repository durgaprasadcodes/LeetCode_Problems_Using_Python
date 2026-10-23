class Solution:
    def maxFrequencyScore(self, nums, k):

        nums.sort()
        ans = l = cost = 0
        for r in range(len(nums)):
            cost += nums[r] - nums[(l + r) // 2]
            while cost > k:
                cost -= nums[((l + 1) + r) // 2] - nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
