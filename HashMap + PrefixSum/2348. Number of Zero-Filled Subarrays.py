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


class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        out = 0
        curr = 0
        for num in nums:
            if num == 0:
                curr += 1
            else:
                out += curr * (curr + 1) // 2 if curr > 0 else 0
                curr = 0
        return out + (curr * (curr + 1) // 2 if curr > 0 else 0)
