class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = ans = 0
        freq = {0:1}
        for num in nums :
            cur_sum += num
            ans += freq.get(cur_sum-k,0)
            freq[cur_sum] = freq.get(cur_sum ,0)+1
        return ans