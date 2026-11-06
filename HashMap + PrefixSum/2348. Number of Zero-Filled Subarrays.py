class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:

        prev = 0
        l = 0
        ans = 0
        for r in range(len(nums)):
            num = nums[r]
            if num == 0:
                if prev != 0:
                    l = r
                ans += r + 1 - l
            prev = num
        return ans
