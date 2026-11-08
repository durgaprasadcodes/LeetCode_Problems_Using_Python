class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cur_sum = 0
        hashmap = {0: 1}
        ans = 0
        for num in nums:
            cur_sum += num
            ans += hashmap.get(cur_sum - k, 0)
            hashmap[cur_sum] = hashmap.get(cur_sum, 0) + 1
        return ans
