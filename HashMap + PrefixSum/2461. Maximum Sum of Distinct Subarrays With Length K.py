class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        
        freq = {}
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i],0)+1

        max_sum = cur_sum if len(freq) == k else 0
        l = 0
        for r in range(k,len(nums)):
            cur_sum += -nums[l]+nums[r] 
            if nums[l] in freq:
                freq[nums[l]] -= 1
                if not freq[nums[l]]:
                    del freq[nums[l]]
            freq[nums[r]] = freq.get(nums[r],0)+1
            if len(freq) == k:
                max_sum = max(max_sum,cur_sum)
            l+=1
        return max_sum