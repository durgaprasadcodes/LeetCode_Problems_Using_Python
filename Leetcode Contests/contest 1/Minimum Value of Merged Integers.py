class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans = float("inf")
        n = len(nums)
        for i in range(0, n, 2):
            merge = str(nums[i]) + str(nums[i + 1])
            ans = min(ans, int(merge))
        return ans
