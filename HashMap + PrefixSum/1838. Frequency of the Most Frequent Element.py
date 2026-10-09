# ===============  BRUTE FORCE ===============


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:

        nums.sort()
        l = 0
        ans = 0
        for i in range(len(nums)):
            diff = 0
            l = 0
            for j in range(0, i):
                diff += nums[i] - nums[j]
            while l < i and diff > k:
                diff -= nums[i] - nums[l]
                l += 1
            ans = max(ans, i - l + 1)
        return ans


# ===============  OPTIMAL SOLUTION ===============


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:

        left = 0
        nums.sort()
        for right in range(len(nums)):
            k += nums[right]
            if k < nums[right] * (right - left + 1):
                k -= nums[left]
                left += 1
        return right - left + 1
