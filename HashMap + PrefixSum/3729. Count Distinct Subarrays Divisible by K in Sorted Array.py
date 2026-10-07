class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:

        cur_sum = 0
        ans = 0
        freq = {0: 1}
        for num in nums:
            cur_sum = (cur_sum + num) % k
            ans += freq.get(cur_sum, 0)
            freq[cur_sum] = freq.get(cur_sum, 0) + 1
        i = 0
        n = len(nums)
        while i < n:
            j = i + 1
            while j < n and nums[i] == nums[j]:
                j += 1
            m = j - i
            for length in range(1, m + 1):
                if (length * nums[i]) % k == 0:
                    ans -= m - length
            i = j
        return ans
