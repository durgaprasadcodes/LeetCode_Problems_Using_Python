class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        cur_sum = 0
        n = len(nums)
        hashmap = {0: -1}
        ans = n
        for idx, num in enumerate(nums):
            cur_sum = (cur_sum + num) % p
            reminder = (cur_sum - target) % p
            if reminder in hashmap:
                ans = min(ans, idx - hashmap[reminder])
            hashmap[cur_sum] = idx
        return ans if ans != n else -1
