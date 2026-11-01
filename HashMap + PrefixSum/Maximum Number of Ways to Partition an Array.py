from collections import Counter


class Solution:
    def waysToPartition(self, nums, k):

        n = len(nums)
        total = sum(nums)

        d = [0] * n
        left_sum = 0
        original = 0
        for p in range(1, n):
            left_sum += nums[p - 1]
            right_sum = total - left_sum
            d[p] = left_sum - right_sum
            if d[p] == 0:
                original += 1

        right_d = Counter(d[1:])
        left_d = Counter()
        ans = original

        for i in range(n):

            cnt = right_d[nums[i] - k] + left_d[k - nums[i]]
            ans = max(ans, cnt)

            if i + 1 <= n - 1:
                left_d[d[i + 1]] += 1
                right_d[d[i + 1]] -= 1

        return ans
