class Solution:
    def numOfSubarrays(self, nums: List[int]) -> int:
        MOD = 10**9+7
        odd = cur_sum = 0
        even = 1
        for num in nums:
            cur_sum += num
            if cur_sum%2 == 0:
                even += 1
            else: odd += 1
        return (even*odd)%MOD