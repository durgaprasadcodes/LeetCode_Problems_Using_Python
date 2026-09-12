class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        ans = 0
        hashmap = {0:1}
        for num in nums:
            cur_sum += 1 if num%2 else 0
            if cur_sum - k in hashmap:
                ans += hashmap[cur_sum-k]
            hashmap[cur_sum] =  hashmap.get(cur_sum,0)+1
        return ans