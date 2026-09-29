class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        cur_sum = 0
        l = 0
        ans = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            score = cur_sum*(r-l+1)
            while score >= k:
                cur_sum -= nums[l]
                l += 1
                score = cur_sum*(r-l+1)
            ans += (r-l+1)
        return ans