class Solution1:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 0
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            cost = (r - l + 1) * nums[r] - cur_sum
            while cost > k:
                cur_sum -= nums[l]
                l += 1
                cost = (r - l + 1) * nums[r] - cur_sum
            ans = max(ans, r - l + 1)
        return ans


class Solution2:
    def maxFrequency(self, nums: list[int], k: int) -> int:

        left = 0
        nums.sort()
        for right in range(len(nums)):
            k += nums[right]
            if k < nums[right] * (right - left + 1):
                k -= nums[left]
                left += 1
        return right - left + 1
