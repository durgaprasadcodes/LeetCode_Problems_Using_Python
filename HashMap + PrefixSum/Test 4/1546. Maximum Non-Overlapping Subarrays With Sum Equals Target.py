class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        hashset = {0}
        cur_sum = 0
        ans = 0
        for num in nums:
            cur_sum += num
            if cur_sum-target in hashset:
                ans+=1
                hashset = {0}
                cur_sum = 0
            else:
                hashset.add(cur_sum)
        return ans