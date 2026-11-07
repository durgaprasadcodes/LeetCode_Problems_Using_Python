class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:

        cur_sum = sum(nums)
        max_sum = float("-inf")
        res = []
        n = len(nums)

        for idx in range(n):
            if cur_sum > max_sum:
                max_sum = cur_sum
                res = [idx]

            elif cur_sum == max_sum:
                res.append(idx)

            if nums[idx] == 0:
                cur_sum += 1
            else:
                cur_sum -= 1

        if cur_sum > max_sum:
            return [n]

        if cur_sum == max_sum:
            res.append(n)

        return res
