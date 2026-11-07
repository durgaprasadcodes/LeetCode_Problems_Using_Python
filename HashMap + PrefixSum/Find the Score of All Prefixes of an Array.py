class Solution:
    def findPrefixScore1(self, nums: list[int]) -> list[int]:
        cur_sum = 0
        cur_max = 0
        res = []
        for num in nums:
            cur_max = max(cur_max, num)
            cur_sum += cur_max + num
            res.append(cur_sum)

        return res

    from itertools import accumulate

    def findPrefixScore(self, nums: list[int]) -> list[int]:
        conversion_arr = []

        prefix_max = 0
        for num in nums:
            if prefix_max < num:
                prefix_max = num
            conversion_arr.append(prefix_max + num)

        return accumulate(conversion_arr)
