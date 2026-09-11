class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<=1:
            return False
        sum_freq = {0:-1}
        cur_sum = 0
        for idx,num in enumerate(nums):
            cur_sum += num
            reminder = cur_sum % k
            if reminder in sum_freq:
                if idx - sum_freq[reminder] >=2:
                    return True
            else:
                sum_freq[reminder] = idx
        return False