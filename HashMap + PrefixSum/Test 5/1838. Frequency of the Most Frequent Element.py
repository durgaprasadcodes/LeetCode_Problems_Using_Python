class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        ans = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            cost = (r-l+1)*nums[r] - cur_sum
            while cost > k:
                cur_sum -= nums[l]
                l+=1
                cost = cur_sum - (r-l+1)*nums[r]
            ans = max(ans,r-l+1)
        return ans