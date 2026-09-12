class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cur_sum = 0
        ans = 0 
        hashmap = {0:1}
        for num in nums:
            cur_sum += num
            if cur_sum - goal in hashmap:
                ans += hashmap[cur_sum - goal]
            hashmap[cur_sum] = hashmap.get(cur_sum,0)+1
        return ans