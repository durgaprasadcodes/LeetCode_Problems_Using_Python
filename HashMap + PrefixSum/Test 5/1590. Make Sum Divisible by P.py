class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        k = sum(nums) % p
        if  k%p == 0:
            return 0
        table = {0:-1}
        cur_sum = 0
        ans = float('inf')
        for idx,num in enumerate(nums):
            cur_sum += num  
            reminder = cur_sum % p
            target = (reminder - k)%p
            if target in table:
                length = idx - table[target]
                if length <len(nums):
                    ans = min(ans,length)
            table[reminder] = idx

        return ans if ans !=float('inf') else -1
