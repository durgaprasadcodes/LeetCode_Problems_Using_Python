class Solution:
    def maxScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == k:
            return sum(nums)
        max_sum = cur_sum = sum(nums[:k])
        l = k-1
        for r in range(n-1,n-k-1,-1):
            cur_sum += (-nums[l]+nums[r])
            max_sum = max(max_sum,cur_sum)
            l -= 1
        return max_sum