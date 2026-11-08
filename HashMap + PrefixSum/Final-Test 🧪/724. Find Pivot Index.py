class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        total = sum(nums)
        cur_sum = 0
        for idx, num in enumerate(nums):
            if cur_sum == total - cur_sum - num:
                return idx
            cur_sum += num
        return -1
