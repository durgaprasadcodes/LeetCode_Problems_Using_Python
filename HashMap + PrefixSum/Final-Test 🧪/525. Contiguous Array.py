class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cur_sum = 0
        ans = 0
        hashmap = {0: -1}

        for idx, num in enumerate(nums):
            cur_sum += 1 if num == 1 else -1

            if cur_sum in hashmap:
                diff = idx - hashmap[cur_sum]
                if diff > ans:
                    ans = diff
            else:
                hashmap[cur_sum] = idx

        return ans
