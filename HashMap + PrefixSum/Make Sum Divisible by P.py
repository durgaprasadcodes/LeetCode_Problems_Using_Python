class Solution:
    def minSubarray(self, nums, p: int) -> int:

        n = len(nums)

        total_r = sum(nums)

        if total_r < p:
            return -1

        total_r %= p
        if total_r == 0:
            return 0
        
        res = n
        cur_r = 0
        r_idx = { 0: -1 }   
        for i in range(n):
            cur_r = (cur_r + nums[i]) % p
            pair_r = (cur_r - total_r + p) % p
            if pair_r in r_idx:
                res = min(res, i-r_idx[pair_r])
            r_idx[cur_r] = i

        return res if res < n else -1
        