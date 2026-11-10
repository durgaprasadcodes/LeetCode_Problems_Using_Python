class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        # if sum(nums) < target:
        #     return 0

        ans = float("inf")
        cur_sum = 0
        hashmap = {}
        l = 0
        for r, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= target:
                ans = min(ans, r - l + 1)
                cur_sum -= nums[l]
                l += 1
        return ans if ans != float("inf") else 0
