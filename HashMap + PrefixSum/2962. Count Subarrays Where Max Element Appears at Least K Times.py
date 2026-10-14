class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        max_num = max(nums)
        n = len(nums)
        ans = 0
        freq = 0
        l = 0
        for r,num in enumerate(nums):
            if num == max_num:
                freq += 1
            while freq>=k:
                ans += n-r
                if nums[l] == max_num:
                    freq -= 1
                l += 1
        return ans

        # ans = 0
        # max_num = max(nums)
        # freq = {}
        # l = 0
        # n = len(nums)
        # for r in range(len(nums)):

        #     freq[nums[r]] = freq.get(nums[r],0)+1

        #     while freq.get(max_num,0) >= k:
        #         ans += n-r
        #         freq[nums[l]] -= 1
        #         l += 1

        # return ans