class Solution:
    def numOfSubarrays(self, nums: List[int]) -> int:
        MOD = 10**9+7

        prefix = 0
        odd = 0
        even = 1
        for num in nums:
            prefix += num
            if prefix%2==0 :
                even += 1
            else:
                odd += 1
        return (even*odd)%MOD
