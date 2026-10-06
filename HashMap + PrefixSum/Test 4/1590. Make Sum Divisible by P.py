class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        k = sum(nums)%p
        if k == 0:
            return 0
        table = {0:-1}
        cur_sum = 0
        min_len = float('inf')
        for i in range(len(nums)):
            cur_sum += nums[i]
            reminder = (cur_sum)%p
            target = (reminder-k)%p
            if target in table :
                length = i - table[target]
                if length < len(nums):
                    min_len = min(min_len,length)
            table[reminder] = i

        return min_len if min_len != float('inf') else -1