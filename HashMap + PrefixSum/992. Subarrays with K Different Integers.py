class Solution1:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def subarraysWithLessThanK(nums, k):
            if k == 0:
                return 0
            l = 0
            ans = 0
            freq = {}
            for r in range(len(nums)):
                num = nums[r]
                freq[num] = freq.get(num, 0) + 1
                while l < r and len(freq) > k:
                    num = nums[l]
                    freq[num] -= 1
                    if freq[num] == 0:
                        del freq[num]
                    l += 1
                ans += r - l + 1
            return ans

        return subarraysWithLessThanK(nums, k) - subarraysWithLessThanK(nums, k - 1)
