class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        l = 0
        max_len = 0
        cal_zeros = 0

        for r in range(len(nums)):
            cal_zeros+=1 if nums[r]==0 else 0
            while cal_zeros>1:
                if nums[l] == 0:
                    cal_zeros-=1
                l+=1
            max_len=max(max_len,r-l+1)

        return max_len-1

                 
s=Solution()
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))